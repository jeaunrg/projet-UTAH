from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from inclusion.models import Patient
from inclusion.forms import CreatePatientFileForm, UpdatePatientFileForm
from account.models import Account
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from inclusion.utils import get_patients_page
from .tasks import calculation_task

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
    patient = get_object_or_404(Patient, slug=slug)
    context = patient.getInfos()
    print(context)
    if request.method == 'POST':
        task = calculation_task.delay(1)
        task_id = task.task_id
        context['task_id'] = task_id

    hm = int(context['height'] / 100)
    context['height'] = "{0}m{1}".format(hm, int(context['height'] - hm*100))
    context['age'] = ((context['ddi'] - context['ddn']) / 365).days
    context['author'] = patient.author
    context['result'] = "Génial!"
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
