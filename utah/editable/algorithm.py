
help = """
Ce fichier contient toute l'architecture de l'algorithme.

Pour associer chaque conclusion à un ou plusieurs traitements, il est nécessaire
d'utiliser des 'références'. Celles-ci sont inclus avec le symbole '%' dans les questions
précédents les conclusions.
Par exemple:
    Pour associer la première conclusion 'Arrêt ou non du traitement.' au traitement
    de l'"aspirine en prévention primaire", il faut ajouter '%ref_aspirin1' à la question précédante ('bleeding_risk').
    Donc 'bleeding_risk %ref_aspirin1'.
    Ainsi cette conclusion fera référence à ce traitement particulier.


L'algorithme est défini par récurrence comme ceci:

'questionId_1': {
    'réponse_11': {
        'questionId_11 %reference_traitement_A': {
            'réponse_111': 'conclusion_111',
            'réponse_112': 'conclusion_112'
        }
    },
    'réponse_12': {
        'questionId_12': {
            ...
        }
    }
}


!! Attention !!
A ne pas oublier de virgules

"""

ALGO = {
    'algo #1': {
        'Français': {
            'antiplatelets #2': {
                'Oui': {
                    'aspirin1 #3': {
                        'Oui': {
                            'bleeding_risk %ref_aspirin1 #4': {
                                'faible': 'Arrêt ou non du traitement.',
                                'intermédiaire': 'Arrêt du traitement.',
                                'élevé': 'Arrêt du traitement.'
                            }
                        }
                    },
                    'aspirin_mono #6': {
                        'Oui': {
                            'bleeding_risk %ref_aspirin_mono #8': {
                                'faible': "Pas d'arrêt du traitement.",
                                'intermédiaire': "Pas d'arrêt du traitement.",
                                'élevé': "Arrêt du traitement."
                            }
                        }
                    },
                    'clopi_mono #9':{
                        'Oui': {
                            'bleeding_risk %ref_clopi_mono #10': {
                                'faible': "Pas d'arrêt du traitement.",
                                'intermédiaire': "Arrêt du traitement. Bridge par l'aspirine.",
                                'élevé': 'Arrêt du traitement.'
                            }
                        }
                    },
                    'stent_bitherapy #11': {
                        'Oui': {
                            'stent_condition #12': {
                                'Oui': {
                                    'bleeding_risk %ref_stent_bitherapy #13': {
                                        'faible': "Report de la procédure. Si impossible, poursuite de la bitherapie.",
                                        'intermédiaire': "Report de la procédure. Si impossible, arrêt de l'anti-P2Y12, pas d'arrêt de l'aspirine.",
                                        'élevé': "Report de la procédure. Si impossible, arrêt de la bitherapie."
                                    }
                                },
                                'Non': {
                                    'bleeding_risk %ref_stent_bitherapy #14': {
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
                    'thromboembolism_risk %ref_vka #16': {
                        'faible': "Pas d'arrêt du traitement.",
                        'élevé': {
                            'bleeding_risk2 %ref_vka #17': {
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
                            'bleeding_risk2 %ref_doac #20': {
                                'faible': "Pas de prise la nuit avant ou le matin du geste invasive. Pas de bridge. Pas de dosage.",
                                'élevé': {
                                    'xaban #21': {
                                        'Oui': {
                                            'cockroft_1 %ref_xaban #22': {
                                                'Oui': 'dernière prise à J-3. Pas de bridge. Pas de dosage.'
                                            }
                                        }
                                    },
                                    'dabigatran #23': {
                                        'Oui': {
                                            'cockroft_2 %ref_dabigatran #24': {
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
                            'bleeding_risk2 %ref_doac #26': {
                                'faible': "Reprise au moment habituel et au moins 6 heures après la fin de la procédure.",
                                'élevé': {
                                    'venous_thrombo %ref_doac #27': {
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
