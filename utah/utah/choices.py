ALGO_CHOICES = ['Belge', 'Français', 'Européen']

BLEEDRISK_CHOICES = ['faible', 'intermédiaire', 'élevé']

INOBS_CHOICES = ["Pas d'inobservance", "Oubli", "Incompréhension", "Contre-ordre médical"]

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

PATH_CHOICES = [
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
]

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
