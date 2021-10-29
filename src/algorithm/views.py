from django.shortcuts import render, get_object_or_404
from patient.models import Patient
from patient.models import TRAIT_CHOICES, PATH_CHOICES
import json

def algo_view(request, slug):
    context = {}
    context['slug'] = slug

    context['initial_responses'] = json.dumps({'traitement1': 'Aspirine, Asaflow, Cardioaspirine'})

    context['questions'] = {
        'traitement1': {
            'question': "Premier traitement ?",
            'answers': TRAIT_CHOICES
        },
        'traitement2': {
            'question': "Deuxième traitement ?",
            'answers': ['Aucun'] + list(TRAIT_CHOICES.keys())
        },
        'pathologie': {
            'question': "Quelle pathologie ?",
            'answers': PATH_CHOICES
        },
        'stent_condition': {
            'answers': ["Stent <1 mois ?", "Stent <6 mois avec un haut risque de thrombose ?", "Infarctus du myocarde <6 mois ?", "Autres"]
        },
        'cockroft_1': {
            'question': 'Cockroft > 30mL/min',
            'answers': ["Oui", "Non"]
        },
        'cockroft_2': {
            'question': 'Cockroft',
            'answers': ["<30 mL/min", "30-49 mL/min", "> 50 mL/min"]
        },
        'venous_thrombo': {
            'question': "Un thrombophylaxis veineux est-il indiqué ?"
        },
        'thromboembolism_risk': {
            'question': 'Quel est le risque de thromboemobolisme ?',
            'answers': ['faible', 'élevé']
        },

        'bleeding_risk_1': {
            'question': "Choisissez le risque d'hémorragie pendant de l'opération",
            'answers': ['faible', 'intermédiaire', 'élevé']
        },
        'bleeding_risk_2': {
            'question': "Choisissez le risque d'hémorragie pendant de l'opération",
            'answers': ['faible', 'élevé']
        }

    }
    return render(request, 'algorithm/algo.html', context)
