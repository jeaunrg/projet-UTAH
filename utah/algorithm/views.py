from django.shortcuts import render, get_object_or_404, redirect
from patient.models import Patient
from editable.questions import QUESTIONS
from editable.default import get_default_results
from editable.data import REFS
from editable.algorithm import ALGO
from django.contrib.auth.decorators import login_required
from .utils import get_algo
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
        # empty conclusions
        patient.reset_cure_conclusions()
        for k, v in conclusions.items():
            if k in REFS:
                traitement_ids = patient.get_traitement_ids(**REFS[k])
                for i in traitement_ids:
                    patient.traitements[i]['conclusion'].append(v)

        patient.save()
        return redirect('patient:detail', slug)

    default_results = {}

    context['refs'] = REFS
    context['algo'], context['pbar_max'] = get_algo()
    context['questions'] = QUESTIONS
    if mode == 'from_scratch':
        context['results'] = {}
    else:
        context['results'] = get_default_results(patient)
    return render(request, 'algorithm/algo_manager.html', context)
