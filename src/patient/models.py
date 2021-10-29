from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.forms import ModelForm

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
    "Acénocoumarol, SINTROM"              : "Anticoagulant-ACOD-AVK",
    "Phenprocoumone, MARCOUMAR"           : "Anticoagulant-ACOD-AVK",
    "Warfarine, MAREVAN"                  : "Anticoagulant-ACOD-AVK",
    "Apixaban, ELIQUIS"                   : "Anticoagulant-ACOD-AOD",
    "Dabigatran, PRADAXA"                 : "Anticoagulant-ACOD-AOD",
    "Edoxaban, LIXIANA"                   : "Anticoagulant-ACOD-AOD",
    "Rivaroxaban, XARELTO"                : "Anticoagulant-ACOD-AOD",
    "Fondaparinux, ARIXTRA"               : "Anticoagulant-ACOD-AOD",
    "Enoxaparine, CLEXANE"                : "Anticoagulant-Injectable",
    "Nadroparine, FRAXIPARINE, FRAXODI"   : "Anticoagulant-Injectable",
    "Tinzaparine, INNOHEP"                : "Anticoagulant-Injectable",
    "HNF, Héparine Sodique"               : "Anticoagulant-Injectable"
}

def to_choice(data):
    if isinstance(data, dict):
        return [(i, i) for i in data.keys()]
    else:
        return [(i, i) for i in data]

class Patient(models.Model):
    incl_num = models.AutoField(primary_key=True)
    height = models.IntegerField('taille')
    weight = models.IntegerField('poids')
    ddn = models.DateTimeField('Date de naissance')
    ddi = models.DateTimeField("Date de l'intervention")
    intervention = models.CharField('intervention', max_length=200, default="")
    chirurgie = models.CharField("Discipline de l'intervention", max_length=40, choices=to_choice(CHIR_CHOICES), default='Chirurgie Cardiaque')
    pathologie = models.CharField("Pathologie justifiant le traitement", max_length=40, choices=to_choice(PATH_CHOICES), default='Prévention primaire')
    traitement1 = models.CharField("Premier traitement", max_length=40, choices=to_choice(TRAIT_CHOICES), default='Aspirine, Asaflow, Cardioaspirine')
    traitement2 = models.CharField("Deuxième traitement", max_length=40, choices=[('Aucun', 'Aucun')] + to_choice(TRAIT_CHOICES), default='Aucun')

    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return str(self.incl_num)

    def save(self, *args, **kwargs):
        super(Patient, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify('patient') + "-" + str(self.incl_num)
            self.save()

    def getInfos(self):
        return {k: v for k, v in self.__dict__.items() if k != '_state'}
