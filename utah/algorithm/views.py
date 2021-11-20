from django.shortcuts import render, get_object_or_404, redirect
from patient.models import Patient
from algorithm.questions import QUESTIONS, ALGO
from django.contrib.auth.decorators import login_required
import json

def get_default_responses(patient):
    default = {k: v for k, v in patient.__dict__.items() if isinstance(v, (str, int, float, bool))}
    return json.dumps(default)

@login_required(login_url='login')
def algo_view(request, slug):
    context = {}
    patient = get_object_or_404(Patient, slug=slug)
    context['patient'] = patient

    if request.POST:
        patient.algo_complete_results = {k: v for k, v in request.POST.items() if k != 'csrfmiddlewaretoken'}
        for k, v in request.POST.items():
            if k in patient.__dict__:
                patient.__dict__[k] = v
        patient.save()
        return redirect('patient:detail', slug)

    context['questions'] = QUESTIONS
    context['default_responses'] = get_default_responses(patient)
    context['auto_skip'] = False
    context['algo'] = json.dumps(ALGO)
    context['quests'] = json.dumps(QUESTIONS)    
    return render(request, 'algorithm/manager.html', context)
