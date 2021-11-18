from django.shortcuts import render, get_object_or_404, redirect
from patient.models import Patient
from algorithm.questions import QUESTIONS
from django.contrib.auth.decorators import login_required
import json


@login_required(login_url='login')
def algo_view(request, slug):
    context = {}
    patient = get_object_or_404(Patient, slug=slug)
    context['slug'] = slug
    context['incl_num'] = patient.incl_num

    if request.POST:
        patient.algo_complete_results = {k: v for k, v in request.POST.items() if k != 'csrfmiddlewaretoken'}
        for k, v in request.POST.items():
            if k in patient.__dict__:
                patient.__dict__[k] = v
        patient.save()
        return redirect('patient:detail', slug)

    context['default_responses'] = json.dumps(patient.get_serializable_infos())
    context['auto_skip'] = False
    context['questions'] = QUESTIONS
    return render(request, 'algorithm/manager.html', context)
