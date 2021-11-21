from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PreopPatientFileForm, PostopPatientFileForm, UpdatePatientFileForm, TraitementFileForm
from account.models import Account
from django.contrib.auth.decorators import login_required
from .utils import get_patients_page
from utah.choices import TRAIT_CHOICES
from datetime import datetime

N_PATIENTS_PER_PAGE = 10


@login_required(login_url='login')
def select_patient_view(request, op):
    context = {'op': op}

    if request.POST:
        incl_num = request.POST['incl_num']
        if Patient.objects.filter(pk=incl_num).exists():
            patient = Patient.objects.get(pk=incl_num)
            if op == 'preop':
                return redirect("algorithm:algo", patient.slug)
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
        patient = form.save(commit=False)
        uname = request.user.username
        author = Account.objects.filter(username=uname).first()
        patient.consultant = uname
        patient.author = author
        patient.save()
        return redirect("patient:detail", patient.slug)

    context['form'] = form
    return render(request, "patient/preop_patient.html", context)



@login_required(login_url='login')
def detail_patient_view(request, slug):
    patient = get_object_or_404(Patient, slug=slug)
    context = {}
    context['patient'] = patient
    return render(request, 'patient/detail_patient.html', context)


@login_required(login_url='login')
def edit_patient_view(request, slug):
    context = {}
    patient = get_object_or_404(Patient, slug=slug)
    form = UpdatePatientFileForm(request.POST or None, instance=patient)

    if request.POST:
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            return redirect("patient:detail", slug)

    context['patient'] = patient
    context['form'] = form
    context['format_date'] = True
    return render(request, 'patient/edit_patient.html', context)


@login_required(login_url='login')
def add_traitement_view(request, slug):
    context = {}
    patient = get_object_or_404(Patient, slug=slug)
    context['patient'] = patient

    form = TraitementFileForm(request.POST or None)
    context['form'] = form

    if request.POST:
        if form.is_valid():
            idtrt = 0
            while str(idtrt) in patient.traitements:
                idtrt += 1
            values = {k: v for k, v in request.POST.items() if k in form.fields}
            if values['traitement'] in TRAIT_CHOICES:
                values['categorie'] = TRAIT_CHOICES.get(values['traitement']).split('-')[0]
            patient.traitements[idtrt] = values
            patient.save()
            return redirect("patient:detail", slug)
    return render(request, 'patient/add_traitement.html', context)

@login_required(login_url='login')
def edit_traitement_view(request, slug, idtrt):
    context = {}
    patient = get_object_or_404(Patient, slug=slug)
    context['patient'] = patient

    form = TraitementFileForm(request.POST or patient.traitements[idtrt])
    if request.POST:

        if form.is_valid():
            if request.POST.get('submitType') == "reset" and 'conclusion' in patient.traitements[idtrt]:
                del patient.traitements[idtrt]['conclusion']
            elif request.POST.get('submitType') == "delete":
                del patient.traitements[idtrt]
            else:
                values = {k: v for k, v in request.POST.items() if k in form.fields}
                if values['traitement'] in TRAIT_CHOICES:
                    values['categorie'] = TRAIT_CHOICES.get(values['traitement']).split('-')[0]
                patient.traitements[idtrt] = values
            patient.save()
            return redirect("patient:detail", slug)

    context['form'] = form
    context['traitement'] = patient.traitements[idtrt]

    return render(request, 'patient/edit_traitement.html', context)


@login_required(login_url='login')
def postop_patient_view(request, slug):
    patient = get_object_or_404(Patient, slug=slug)
    context = {}

    form = PostopPatientFileForm(request.POST or None, instance=patient)
    if request.POST:
        if form.is_valid():
            patient = form.save(commit=False)
            author = Account.objects.filter(username=request.user.username).first()
            patient.author = author
            for k, v in request.POST.items():
                for label in ['ddprise_pr', 'inobservance']:
                    if k.startswith(label):
                        idtrt = k.split('__')[-1]
                        patient.traitements[idtrt][label] = v

            patient.save()
            return redirect("patient:detail", patient.slug)

    context['slug'] = slug
    context['form'] = form
    context['patient'] = patient
    return render(request, "patient/postop_patient.html", context)


@login_required(login_url='login')
def patients_view(request, filter):
    context = {}
    query, patients = get_patients_page(request, N_PATIENTS_PER_PAGE, filter)
    context['patients'] = patients
    context['n_patients'] = len(patients)
    if query:
        context['query'] = query

    return render(request, 'patient/patients.html', context)
