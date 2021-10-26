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
    "Prevention primaire",
    "Prevention secondaire",
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

TRAIT_CHOICES = [
    "Aspirine, Asaflow, Cardioaspirine",
    "Clopidogrel, PLAVIX",
    "Prasugrel, EFFIENT",
    "Ticlopidine, TICLID",
    "Dipyridamole",
    "Ticagrelor, BRILIQUE",
    "Acénocoumarol, SINTROM",
    "Phenprocoumone, MARCOUMAR",
    "Warfarine, MAREVAN",
    "Apixaban, ELIQUIS",
    "Dabigatran, PRADAXA",
    "Edoxaban, LIXIANA",
    "Rivaroxaban, XARELTO",
    "Enoxaparine, CLEXANE",
    "Nadroparine, FRAXIPARINE, FRAXODI",
    "Tinzaparine, INNOHEP",
    "Fondaparinux, ARIXTRA",
    "HNF, Héparine Sodique"
]

def list2choices(list):
    return [(i, i) for i in list]

class Patient(models.Model):
    incl_num = models.AutoField(primary_key=True)
    height = models.IntegerField('taille')
    weight = models.IntegerField('poids')
    ddn = models.DateTimeField('Date de naissance')
    ddi = models.DateTimeField("Date de l'intervention")
    intervention = models.CharField('intervention', max_length=200, default="")
    chirurgie = models.CharField("Discipline de l'intervention", max_length=40, choices=list2choices(CHIR_CHOICES), default='Chirurgie Cardiaque')
    pathologie = models.CharField("Pathologie justifiant le traitement", max_length=40, choices=list2choices(PATH_CHOICES), default='Prevention primaire')
    traitement1 = models.CharField("Premier traitement", max_length=40, choices=list2choices(TRAIT_CHOICES), default='Aspirine, Asaflow, Cardioaspirine')
    traitement2 = models.CharField("Deuxième traitement", max_length=40, choices=list2choices(['Aucun']+TRAIT_CHOICES), default='Aucun')

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
