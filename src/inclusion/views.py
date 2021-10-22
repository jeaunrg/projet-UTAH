from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from inclusion.models import Patient
from inclusion.forms import CreatePatientFileForm, UpdatePatientFileForm
from account.models import Account
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from inclusion.utils import get_patients_page


@login_required(login_url='login')
def create_patient_file_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    patient_form = CreatePatientFileForm(request.POST or None)
    if patient_form.is_valid():
        obj = patient_form.save(commit=False)
        author = Account.objects.filter(username=user.username).first()
        obj.author = author
        obj.save()
        return redirect("inclusion:detail", obj.slug)

    context['patient_form'] = patient_form

    return render(request, "inclusion/create_patient_file.html", context)


@login_required(login_url='login')
def detail_patient_file_view(request, slug):
    context = {}

    user = request.user

    patient_file = get_object_or_404(Patient, slug=slug)

    if request.POST:
        form = UpdatePatientFileForm(request.POST or None, request.FILES or None, instance=patient_file)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            patient_file = obj


    form = UpdatePatientFileForm(initial=patient_file.__dict__)
    context['id'] = patient_file.id
    context['author'] = patient_file.author
    context['date_updated'] = patient_file.date_updated
    context['slug'] = patient_file.slug

    context['patient_form'] = form
    return render(request, 'inclusion/detail_patient_file.html', context)


@login_required(login_url='login')
def edit_patient_file_view(request, slug):

    context = {'editable': False}

    user = request.user

    patient_file = get_object_or_404(Patient, slug=slug)

    if request.POST:
        form = UpdatePatientFileForm(request.POST or None, instance=patient_file)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect("inclusion:detail", slug)

    form = UpdatePatientFileForm(initial=patient_file.__dict__)
    context['id'] = patient_file.id
    context['slug'] = patient_file.slug
    context['patient_form'] = form
    return render(request, 'inclusion/edit_patient_file.html', context)


@login_required(login_url='login')
def patients_view(request, filter):
    context = {}
    query, patients = get_patients_page(request, 3, filter)
    context['patients'] = patients
    context['n_patients'] = len(patients)
    if query:
        context['query'] = query

    return render(request, 'inclusion/patients.html', context)
