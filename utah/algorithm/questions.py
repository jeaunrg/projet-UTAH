from utah.choices import *

QUESTIONS = {
    'algo': {
        'question': "Quel algorithme voulez-vous suivre ?",
        'answers': ALGO_CHOICES
    },
    'traitement1': {
        'question': "Premier traitement ?",
        'answers': TRAIT_CHOICES
    },
    'traitement2': {
        'question': "Deuxième traitement ?",
        'answers': TRAIT_CHOICES
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
        'question': "Choisissez le risque d'hémorragie pendant l'opération",
        'answers': ['faible', 'intermédiaire', 'élevé']
    },
    'bleeding_risk_2': {
        'question': "Choisissez le risque d'hémorragie pendant l'opération",
        'answers': ['faible', 'élevé']
    }
}
