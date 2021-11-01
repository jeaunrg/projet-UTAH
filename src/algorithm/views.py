from django.shortcuts import render, get_object_or_404, redirect
from patient.models import Patient
from patient.data import QUESTIONS
import json

def algo_view(request, slug):
    context = {}
    patient = get_object_or_404(Patient, slug=slug)
    context['slug'] = slug

    if request.POST:
        patient.resultats = {k: v for k, v in request.POST.items() if k != 'csrfmiddlewaretoken'}
        patient.save()
        return redirect('patient:detail', slug)

    context['default_responses'] = json.dumps(patient.getSerializableInfos())
    context['auto_skip'] = False;

    context['questions'] = QUESTIONS
    return render(request, 'algorithm/manager.html', context)
