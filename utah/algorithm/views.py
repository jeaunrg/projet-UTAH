from django.shortcuts import render, get_object_or_404, redirect
from patient.models import Patient
from algorithm.questions import QUESTIONS, ALGO, REFS
from django.contrib.auth.decorators import login_required
import json


def get_default_results(patient):
    results = {'antiplatelets': 'Non', 'aspirin1': 'Non', 'aspirin_mono': 'Non',
               'clopi_mono': 'Non', 'stent_bitherapy': 'Non', 'vka': 'Non', 'doac': 'Non',
               'xaban': 'Non', 'dabigatran': 'Oui'}

    for values in patient.traitements.values():
        if 'Antiagregant plaquettaire' in values['categorie']:
            results['antiplatelets'] = 'Oui'
        if values['traitement'] == "Aspirine, Asaflow, Cardioaspirine" and values['pathologie'] == "Prévention primaire":
            results['aspirin1'] = 'Oui'
        if values['traitement'] == "Aspirine, Asaflow, Cardioaspirine" and values['pathologie'] == "Prévention secondaire":
            results['aspirin_mono'] = 'Oui'
        if values['traitement'] == "Clopidogrel, PLAVIX" and values['pathologie'] == "Prévention secondaire":
            results['clopi_mono'] = 'Oui'

        if values['pathologie'] == "Stents Cardiaques":
            results['stent_bitherapy'] = 'Oui'

        if 'AVK' in values['categorie']:
            results['vka'] = 'Oui'

        if 'ACOD' in values['categorie']:
            results['doac'] = 'Oui'

        if 'xaban' in values['categorie']:
            results['xaban'] = 'Oui'

        if values['traitement'] == "Dabigatran, PRADAXA":
            results['dabigatran'] = 'Oui'


    results['before'] = 'Oui'
    results['after'] = 'Oui'
    if patient.bleeding_risk:
        results['bleeding_risk'] = patient.bleeding_risk
        if patient.bleeding_risk != 'intermédiaire':
            results['bleeding_risk2'] = patient.bleeding_risk
    return results

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
    return render(request, 'algorithm/manager.html', context)
