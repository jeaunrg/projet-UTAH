from utah.choices import *

QUESTIONS = {
    'algo': {
        'question': "Quel algorithme voulez-vous suivre ?",
        'answers': ALGO_CHOICES
    },

    #--------------------- ANTIPLATELETS ------------------------------#
    'antiplatelets': {
        'question': 'Le patient prend-il des anti-agrégants plaquettaires ?',
        'answers': ['Oui', 'Non']
    },
    'aspirin1': {
        'details': {'pathologie': "Prévention primaire", "traitement": "Aspirine, Asaflow, Cardioaspirine"},
        'question': "Aspirine en prévention primaire ?",
        'answers': ['Oui', 'Non']
    },
    'apa2': {
        'question': "APA en prévention secondaire ?",
        'answers': ['Oui', 'Non']
    },
    'aspirin_mono': {
        'details': {'pathologie': "Prévention secondaire", "traitement": "Aspirine, Asaflow, Cardioaspirine"},
        'question': "Aspirine en monotherapy ?",
        'answers': ['Oui', 'Non']
    },
    'clopi_mono': {
        'details': {'pathologie': "Prévention secondaire", "traitement": "Clopidogrel, PLAVIX"},
        'question': "Clopidogrel en monotherapy ?",
        'answers': ['Oui', 'Non']
    },
    'stent_bitherapy': {
        'details': {'pathologie': "Stents Cardiaques"},
        'question': "Bithérapie pour les stents coronaires ?",
        'answers': ['Oui', 'Non']
    },
    'stent_condition': {
        'question': """Un de ces critères est-il vrai ?
    Stent <1 mois
    Stent <6 mois avec un haut risque de thrombose
    Infarctus du myocarde <6 mois""",
        'answers': ['Oui', 'Non']
    },

    #--------------------- VKA ------------------------------#
    'vka': {
        'details': {"categorie": "Anticoagulant-ACOD-AVK"},
        'question': 'Le patient prend-il des VKA ?',
        'answers': ['Oui', 'Non']
    },
    'thromboembolism_risk': {
        'question': 'Quel est le risque de thromboemobolisme ?',
        'answers': ['faible', 'élevé']
    },

    #--------------------- DOAC ------------------------------#
    'doac': {
        'question': 'Le patient prend-il des DOAC ?',
        'answers': ['Oui', 'Non']
    },
    'before': {
        'details': {"categorie": "Anticoagulant-ACOD", "more": "before"},
        'question': 'Avant la procédure',
        'answers': ["Oui"]
    },
    'after': {
        'details': {"categorie": "Anticoagulant-ACOD", "more": "after"},
        'question': 'Après la procédure',
        'answers': ["Oui"]
    },
    'xaban': {
        'details': {"traitement": "Apixaban, ELIQUIS | Edoxaban, LIXIANA | Rivaroxaban, XARELTO", "more": "before"},
        'question': 'Le patient prend-il des xaban ?',
        'answers': ['Oui', 'Non']
    },
    'dabigatran': {
        'details': {"traitement": "Dabigatran, PRADAXA", "more": "before"},
        'question': 'Le patient prend-il du dabigatran ?',
        'answers': ['Oui', 'Non']
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
        'question': "Un thrombophylaxis veineux est-il indiqué ?",
        'answers': ["Oui", "Non"]
    },

    #--------------------- Autre ------------------------------#
    'bleeding_risk': {
        'question': "Quel est le risque d'hémorragie pendant l'opération ?",
        'answers': ['faible', 'intermédiaire', 'élevé']
    },
    'bleeding_risk2': {
        'question': "Quel est le risque d'hémorragie pendant l'opération ?",
        'answers': ['faible', 'élevé']
    },
}


ALGO = {
    'algo #1': {
        'Français': {
            'antiplatelets #2': {
                'Oui': {
                    'aspirin1 #3': {
                        'Oui': {
                            'bleeding_risk #4': {
                                'faible': 'Arrêt ou non du traitement.',
                                'intermédiaire': 'Arrêt du traitement.',
                                'élevé': 'Arrêt du traitement.'
                            }
                        }
                    },
                    'apa2 #5': {
                        'Oui': {
                            'aspirin_mono #6': {
                                'Oui': {
                                    'bleeding_risk #8': {
                                        'faible': "Pas d'arrêt du traitement.",
                                        'intermédiaire': "Pas d'arrêt du traitement.",
                                        'élevé': "Arrêt du traitement."
                                    }
                                }
                            },
                            'clopi_mono #9':{
                                'Oui': {
                                    'bleeding_risk #10': {
                                        'faible': "Pas d'arrêt du traitement.",
                                        'intermédiaire': "Arrêt du traitement. Bridge par l'aspirine.",
                                        'élevé': 'Arrêt du traitement.'
                                    }
                                }
                            }
                        }
                    },
                    'stent_bitherapy #11': {
                        'Oui': {
                            'stent_condition #12': {
                                'Oui': {
                                    'bleeding_risk #13': {
                                        'faible': "Report de la procédure. Si impossible, poursuite de la bitherapie.",
                                        'intermédiaire': "Report de la procédure. Si impossible, arrêt de l'anti-P2Y12, pas d'arrêt de l'aspirine.",
                                        'élevé': "Report de la procédure. Si impossible, arrêt de la bitherapie."
                                    }
                                },
                                'Non': {
                                    'bleeding_risk #14': {
                                        'faible': "Pas d'arrêt de la bitherapie.",
                                        'intermédiaire': "Arrêt de l'anti-P2Y12. Pas d'arrêt de l'aspirine.",
                                        'élevé': "Arrêt de la bitherapie."
                                    }
                                }
                            }
                        }
                    }
                }
            },
            'vka #15': {
                'Oui': {
                    'thromboembolism_risk #16': {
                        'faible': "Pas d'arrêt du traitement.",
                        'élevé': {
                            'bleeding_risk2 #17': {
                                'faible': "Arrét du traitement à J-3.",
                                'élevé': "Bridge à J-7."
                            }
                        }
                    }
                }
            },
            'doac #18': {
                'Oui': {
                    'before #19': {
                        'Oui': {
                            'bleeding_risk2 #20': {
                                'faible': "Pas de prise la nuit avant ou le matin du geste invasive. Pas de bridge. Pas de dosage.",
                                'élevé': {
                                    'xaban #21': {
                                        'Oui': {
                                            'cockroft_1 #22': {
                                                'Oui': 'dernière prise à J-3. Pas de bridge. Pas de dosage.'
                                            }
                                        }
                                    },
                                    'dabigatran #23': {
                                        'Oui': {
                                            'cockroft_2 #24': {
                                                '> 50 mL/min': 'dernière prise à J-4. Pas de bridge. Pas de dosage.',
                                                '30-49 mL/min': 'dernière prise à J-5. Pas de bridge. Pas de dosage.'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    'after #25': {
                        'Oui': {
                            'bleeding_risk2 #26': {
                                'faible': "Reprise au moment habituel et au moins 6 heures après la fin de la procédure.",
                                'élevé': {
                                    'venous_thrombo #27': {
                                        'Oui': "Anticoagulants à dose prophylactique au moins 6 heures après l'intervention. Anticoagulants à doses curatives dès que l'hémostase le permet.",
                                        'Non': "Anticoagulants à doses curatives dès que l'hémostase le permet."
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "Belge": "A compléter",
        "Européen": "A compléter"
    }
}
