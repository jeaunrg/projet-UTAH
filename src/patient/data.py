CHIR_CHOICES = [
    "Chirurgie Cardiaque",
    "Chirurgie Digestive",
    "Chirurgie Gynecologique",
    "Chirurgie Hepatique",
    "Chirurgie Orthopedique",
    "Chirurgie Ophtalmologique",
    "Chirurgie Plastique",
    "Chirurgie Thoracique",
    "Chirurgie Urologique",
    "Endoscopie",
    "Neurochirurgie",
    "Chirurgie ORL",
    "Radiologie Interventionnelle",
    "Stomatologie"
]

PATH_CHOICES = (
    "Prévention primaire",
    "Prévention secondaire",
    "Fibrilation Atriale",
    "Valvulopathie",
    "Pontages Cardiaques",
    "Chirurgie Vasculaire Arterielle",
    "ATCD EP",
    "ATCD TVP",
    "ATCD AVC + AIT",
    "CMI",
    "Stents Cardiaques",
    "Greffe",
    "Thrombose Porte",
    "Thrombose Mesenterique"
)

TRAIT_CHOICES = {
    "Aspirine, Asaflow, Cardioaspirine"   : "Antiagregant plaquettaire",
    "Clopidogrel, PLAVIX"                 : "Antiagregant plaquettaire",
    "Prasugrel, EFFIENT"                  : "Antiagregant plaquettaire",
    "Ticlopidine, TICLID"                 : "Antiagregant plaquettaire",
    "Dipyridamole"                        : "Antiagregant plaquettaire",
    "Ticagrelor, BRILIQUE"                : "Antiagregant plaquettaire",
    "Acénocoumarol, SINTROM"              : "Anticoagulant-ACOD-AVK-thrombo",
    "Phenprocoumone, MARCOUMAR"           : "Anticoagulant-ACOD-AVK",
    "Warfarine, MAREVAN"                  : "Anticoagulant-ACOD-AVK",
    "Apixaban, ELIQUIS"                   : "Anticoagulant-ACOD-AOD-thrombo-xaban",
    "Dabigatran, PRADAXA"                 : "Anticoagulant-ACOD-AOD-thrombo",
    "Edoxaban, LIXIANA"                   : "Anticoagulant-ACOD-AOD-xaban",
    "Rivaroxaban, XARELTO"                : "Anticoagulant-ACOD-AOD-xaban",
    "Fondaparinux, ARIXTRA"               : "Anticoagulant-ACOD-AOD",
    "Enoxaparine, CLEXANE"                : "Anticoagulant-Injectable",
    "Nadroparine, FRAXIPARINE, FRAXODI"   : "Anticoagulant-Injectable",
    "Tinzaparine, INNOHEP"                : "Anticoagulant-Injectable",
    "HNF, Héparine Sodique"               : "Anticoagulant-Injectable"
}

QUESTIONS = {
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
        'question': "Choisissez le risque d'hémorragie pendant l'opération",
        'answers': ['faible', 'intermédiaire', 'élevé']
    },
    'bleeding_risk_2': {
        'question': "Choisissez le risque d'hémorragie pendant l'opération",
        'answers': ['faible', 'élevé']
    }
}
