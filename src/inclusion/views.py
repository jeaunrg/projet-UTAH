from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from inclusion.models import Patient
from inclusion.forms import CreatePatientFileForm, UpdatePatientFileForm
from account.models import Account
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from inclusion.utils import get_patients_page

N_PATIENTS_PER_PAGE = 10

@login_required(login_url='login')
def create_patient_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreatePatientFileForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(username=user.username).first()
        obj.author = author
        obj.save()
        return redirect("inclusion:detail", obj.slug)

    context['form'] = form
    context['is_editable'] = True
    return render(request, "inclusion/create_patient.html", context)


@login_required(login_url='login')
def detail_patient_view(request, slug):
    context = {}

    user = request.user

    patient = get_object_or_404(Patient, slug=slug)

    if request.POST:
        form = UpdatePatientFileForm(request.POST or None, request.FILES or None, instance=patient)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            patient = obj


    form = UpdatePatientFileForm(initial=patient.__dict__)
    context['incl_num'] = patient.incl_num
    context['author'] = patient.author
    context['date_updated'] = patient.date_updated
    context['slug'] = patient.slug

    context['form'] = form
    context['is_editable'] = False
    return render(request, 'inclusion/detail_patient.html', context)


@login_required(login_url='login')
def edit_patient_view(request, slug):

    context = {'editable': False}

    user = request.user

    patient = get_object_or_404(Patient, slug=slug)

    if request.POST:
        form = UpdatePatientFileForm(request.POST or None, instance=patient)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect("inclusion:detail", slug)

    form = UpdatePatientFileForm(initial=patient.__dict__)
    context['incl_num'] = patient.incl_num
    context['slug'] = patient.slug
    context['form'] = form
    context['is_editable'] = True    
    return render(request, 'inclusion/edit_patient.html', context)


@login_required(login_url='login')
def patients_view(request, filter):
    context = {}
    query, patients = get_patients_page(request, N_PATIENTS_PER_PAGE, filter)
    context['patients'] = patients
    context['n_patients'] = len(patients)
    if query:
        context['query'] = query

    return render(request, 'inclusion/patients.html', context)
