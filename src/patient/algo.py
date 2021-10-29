## Les pathologies doivent être prises dans la liste suivante:
# "Prevention primaire", "Prevention secondaire", "Fibrilation Atriale", "Valvulopathie",
# "Pontages Cardiaques", "Chirurgie Vasculaire Arterielle", "ATCD EP", "ATCD TVP",
# "ATCD AVC + AIT", "CMI", "Stents Cardiaques", "Greffe", "Thrombose Porte", "Thrombose Mesenterique"


def guidelines(traitement1):
    categorie_traitement1 = TRAIT_CHOICES[traitement1]

    if categorie_traitement1 == 'Antiagregant plaquettaire':
        monotherapy = (traitement2 == 'Aucun')

        # conditions
        if pathologie == 'Prevention primaire' and traitement1 == "Aspirine, Asaflow, Cardioaspirine":
            result = ['Stop or Continuation', 'Stop', 'Stop']

        elif pathologie == 'Prevention secondaire' and monotherapy:
            if traitement1 == "Aspirine, Asaflow, Cardioaspirine":
                result = ['Continuation', 'Continuation', 'Stop']
            elif traitement1 == "Clopidogrel, PLAVIX":
                result = ['Continuation', 'Stop, bridge by aspirin', 'Stop']

        elif pathologie == "Stents Cardiaques" and not monotherapy:
            if stent_condition in ['Stent <1 month',
                                   'Stent <6 month with high thrombotic risk',
                                   'Myocardial infarction <6 month']:
                result = ['Postpone the procedure. If impossible, continue the bitherapy',
                          'Postpone the procedure. If impossible, stop the anto-P2Y12, continue the aspirin',
                          'Postpone the procedure. If impossible, stop the bitherapy']
            else:
                result = ['Continue the bitherapy',
                          'Stop the anti-P2Y12, continue the aspirin',
                          'Stop the bitherapy']

        # return result based on input bleeding risk
        risk_index = ['low', 'intermediary', 'high'].index(bleeding_risk)

    elif categorie_traitement1.startswith('Anticoagulant-ACOD'):

        result_before = "No bridge, no dosage."
        if bleeding_risk == 'low':
            result_before += ' No taking the night before or the morning of the invasive gesture.'
            result_after = 'Restart at the usual time and at least 6 hours after the end of the procedure.'
        elif bleeding_risk == 'high':
            if traitement in ["Rivaroxaban, XARELTO", "Apixaban, ELIQUIS", "Edoxaban, LIXIANA"] and cockroft_condition == "Cockcroft > 30mL/min":
                result_before += ' Final take at d-3'
            elif traitement == "Dabigatran, PRADAXA":
                if cockroft_condition == "Cockcroft > 50mL/min":
                    result_before += ' Final take at d-4'
                elif cockroft_condition == "Cockroft 30-49 mL/min":
                    result_before += ' Final take at d-5'

            result_after = "Anticoagulants in curative doses as soon as haemostasis allows it."
            if venous_thrombo:
                result_after += " Anticoagulants at a prophylactic dose at least 6 hours after the procedure."

        if categorie_traitement1 == 'Anticoagulant-ACOD-AVK':
            if thromboembolism_risk == 'low':
                result = 'Continuation'
            elif bleeding_risk == 'low':
                result = 'Stop at J-3'
            elif bleeding_risk == 'high':
                result = 'Bridge at J-7'




def antiplatelets_guidelines(bleeding_risk, pathologie, traitement1, traitement2='Aucun',
                             stent_condition=None):
    """
    Parameters
    ----------
    bleeding_risk: {'low', 'high'}
    pathologie: str
    traitement1: str
    traitement2: str, default='Aucun'
    stent_condition: str or None, default=None

    """
    # initialisation
    result = ['No result'] * 3
    monotherapy = (traitement2 == 'Aucun')

    # conditions
    if pathologie == 'Prevention primaire' and traitement1 == "Aspirine, Asaflow, Cardioaspirine":
        result = ['Stop or Continuation', 'Stop', 'Stop']

    elif pathologie == 'Prevention secondaire' and monotherapy:
        if traitement1 == "Aspirine, Asaflow, Cardioaspirine":
            result = ['Continuation', 'Continuation', 'Stop']
        elif traitement1 == "Clopidogrel, PLAVIX":
            result = ['Continuation', 'Stop, bridge by aspirin', 'Stop']

    elif pathologie == "Stents Cardiaques" and not monotherapy:
        if stent_condition in ['Stent <1 month',
                               'Stent <6 month with high thrombotic risk',
                               'Myocardial infarction <6 month']:
            result = ['Postpone the procedure. If impossible, continue the bitherapy',
                      'Postpone the procedure. If impossible, stop the anto-P2Y12, continue the aspirin',
                      'Postpone the procedure. If impossible, stop the bitherapy']
        else:
            result = ['Continue the bitherapy',
                      'Stop the anti-P2Y12, continue the aspirin',
                      'Stop the bitherapy']

    # return result based on input bleeding risk
    risk_index = ['low', 'intermediary', 'high'].index(bleeding_risk)
    return result[risk_index]


def vka_guidelines(thromboembolism_risk, bleeding_risk='low'):
    """
    Parameters
    ----------
    thromboembolism_risk: {'low', 'high'}
    bleeding_risk: {'low', 'high'}, default='low'

    """

    # initialisation
    result = 'No result'

    # conditions
    if thromboembolism_risk == 'low':
        result = 'Continuation'
    elif bleeding_risk == 'low':
        result = 'Stop at J-3'
    elif bleeding_risk == 'high':
        result = 'Bridge at J-7'

    return result


def doac_guidelines(bleeding_risk, traitement=None, cockroft_condition=None, venous_thrombo=None):
    """
    Parameters
    ----------
    bleeding_risk: {'low', 'high'}
    traitement: str or None, default=None
    cockroft_condition: str or None, default=None
    venous_thrombo: bool or None, default=None
        if True, venous thromboprophylaxis is indicated

    """
    # initialisation
    result_before = result_after = 'No result'

    # conditions
    result_before = "No bridge, no dosage."
    if bleeding_risk == 'low':
        result_before += ' No taking the night before or the morning of the invasive gesture.'
        result_after = 'Restart at the usual time and at least 6 hours after the end of the procedure.'
    elif bleeding_risk == 'high':
        if traitement in ["Rivaroxaban, XARELTO", "Apixaban, ELIQUIS", "Edoxaban, LIXIANA"] and cockroft_condition == "Cockcroft > 30mL/min":
            result_before += ' Final take at d-3'
        elif traitement == "Dabigatran, PRADAXA":
            if cockroft_condition == "Cockcroft > 50mL/min":
                result_before += ' Final take at d-4'
            elif cockroft_condition == "Cockroft 30-49 mL/min":
                result_before += ' Final take at d-5'

        result_after = "Anticoagulants in curative doses as soon as haemostasis allows it."
        if venous_thrombo:
            result_after += " Anticoagulants at a prophylactic dose at least 6 hours after the procedure."

    return {'before': result_before, 'after': result_after}



if __name__ == "__main__":
    print("\nAntiplatelets")
    print(1, antiplatelets_guidelines(bleeding_risk='low',
                                      pathologie='Prevention primaire',
                                      traitement1="Aspirine, Asaflow, Cardioaspirine"))
    print(2, antiplatelets_guidelines(bleeding_risk='intermediary',
                                      pathologie='Prevention secondaire',
                                      traitement1="Clopidogrel, PLAVIX"))
    print(3, antiplatelets_guidelines(bleeding_risk='high',
                                      pathologie='Stents Cardiaques',
                                      traitement1="Apixaban, ELIQUIS",
                                      traitement2="Rivaroxaban, XARELTO",
                                      stent_condition='Stent <1 month'))
    print(4, antiplatelets_guidelines(bleeding_risk='low',
                                      pathologie='Pontages Cardiaques',
                                      traitement1="Aspirine, Asaflow, Cardioaspirine"))

    print("\nVKA")
    print(1, vka_guidelines(thromboembolism_risk='low'))
    print(2, vka_guidelines(bleeding_risk='low',
                            thromboembolism_risk='high'))

    print("\nDOAC")
    print(1, doac_guidelines(bleeding_risk='high',
                             traitement='Rivaroxaban, XARELTO',
                             cockroft_condition='Cockcroft > 30mL/min'))
    print(2, doac_guidelines(bleeding_risk='high',
                             venous_thrombo=True))
    print(3, doac_guidelines(bleeding_risk='low'))
    print(1, doac_guidelines(bleeding_risk='high',
                             traitement='Tinzaparine, INNOHEP'))
