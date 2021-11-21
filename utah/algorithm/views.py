from django.shortcuts import render, get_object_or_404, redirect
from patient.models import Patient
from editable.questions import QUESTIONS
from editable.algorithm import ALGO
from editable.default import get_default_results
from editable.data import REFS
from django.contrib.auth.decorators import login_required
import json


@login_required(login_url='login')
def algo_view(request, slug, mode):
    context = {}
    patient = get_object_or_404(Patient, slug=slug)
    context['patient'] = patient

    if request.POST:
        results = {}
        conclusions = {}
        for k, v in request.POST.items():
            if k.startswith('RESULTS'):
                results[k[8:]] = v
                if k[8:] in patient.__dict__:
                    patient.__dict__[k[8:]] = v
            elif k.startswith('CONCLUSIONS'):
                conclusions[k[12:]] = v
        patient.algo_complete_results = results

        for k, v in conclusions.items():
            if k in REFS:
                traitement_ids = patient.get_traitement_ids(**REFS[k])
                for i in traitement_ids:
                    patient.traitements[i]['conclusion'] = v
        patient.save()
        return redirect('patient:detail', slug)

    default_results = {}

    context['questions'] = QUESTIONS
    context['refs'] = REFS
    context['algo'] = json.dumps(ALGO)
    context['quests'] = json.dumps(QUESTIONS)
    if mode == 'from_scratch':
        context['results'] = {}
    else:
        context['results'] = get_default_results(patient)
    return render(request, 'algorithm/algo_manager.html', context)
