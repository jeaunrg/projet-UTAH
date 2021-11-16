from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PreopPatientFileForm, PostopPatientFileForm, UpdatePatientFileForm
from account.models import Account
from django.contrib.auth.decorators import login_required
from .utils import get_patients_page
from .data import TRAIT_CHOICES

N_PATIENTS_PER_PAGE = 10


@login_required(login_url='login')
def select_patient_view(request, op):
    context = {'op': op}

    if request.POST:
        num_incl = request.POST['num_incl']
        if Patient.objects.filter(pk=num_incl).exists():
            patient = Patient.objects.get(pk=num_incl)
            print(patient.slug)
            if op == 'preop':
                return redirect("patient:preop")
                return
            if op == 'postop':
                return redirect("patient:postop", patient.slug)
        else:
            context['error'] = "Aucun patient n'a ce numéro d'inclusion."
    return render(request, "patient/select_patient.html", context)


@login_required(login_url='login')
def preop_patient_view(request):
    context = {}

    form = PreopPatientFileForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(username=request.user.username).first()
        obj.author = author
        obj.save()
        return redirect("patient:detail", obj.slug)

    context['form'] = form
    context['is_editable'] = True
    return render(request, "patient/preop_patient.html", context)


@login_required(login_url='login')
def postop_patient_view(request, slug):
    patient = get_object_or_404(Patient, slug=slug)
    context = {}

    form = PostopPatientFileForm(request.POST or None, instance=patient)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(username=request.user.username).first()
        obj.author = author
        obj.save()
        return redirect("patient:detail", obj.slug)

    context['slug'] = slug
    context['form'] = form
    context['patient'] = patient
    context['categorie'] = TRAIT_CHOICES
    context['is_editable'] = True
    return render(request, "patient/postop_patient.html", context)


@login_required(login_url='login')
def detail_patient_view(request, slug):
    patient = get_object_or_404(Patient, slug=slug)
    context = patient.get_infos()

    hm = int(context['height'] / 100)
    context['height'] = "{0}m{1}".format(hm, int(context['height'] - hm * 100))
    context['age'] = ((context['ddi'] - context['ddn']) / 365).days
    context['patient'] = patient
    return render(request, 'patient/detail_patient.html', context)


@login_required(login_url='login')
def edit_patient_view(request, slug):
    context = {'editable': False}

    patient = get_object_or_404(Patient, slug=slug)

    if request.POST:
        form = UpdatePatientFileForm(request.POST or None, instance=patient)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect("patient:detail", slug)

    form = UpdatePatientFileForm(initial=patient.get_infos())
    context['incl_num'] = patient.incl_num
    context['slug'] = patient.slug
    context['form'] = form
    context['is_editable'] = True
    return render(request, 'patient/edit_patient.html', context)


@login_required(login_url='login')
def patients_view(request, filter):
    context = {}
    query, patients = get_patients_page(request, N_PATIENTS_PER_PAGE, filter)
    context['patients'] = patients
    context['n_patients'] = len(patients)
    if query:
        context['query'] = query

    return render(request, 'patient/patients.html', context)