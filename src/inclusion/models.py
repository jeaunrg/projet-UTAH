from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.forms import ModelForm

CHIR_CHOICES = (
    ("CCA", "Chirurgie Cardiaque"),
    ("CDI", "Chirurgie Digestive"),
    ("CGY", "Chirurgie Gynecologique"),
    ("CHE", "Chirurgie Hepatique"),
    ("COR", "Chirurgie Orthopedique"),
    ("COP", "Chirurgie Ophtalmologique"),
    ("CPL", "Chirurgie Plastique"),
    ("CTH", "Chirurgie Thoracique"),
    ("CUR", "Chirurgie Urologique"),
    ("END", "Endoscopie"),
    ("NEU", "Neurochirurgie"),
    ("ORL", "Chirurgie ORL"),
    ("RIN", "Radiologie Interventionnelle"),
    ("STO", "Stomatologie")
)

PATH_CHOICES = (
    ("PPR", "Prevention primaire"),
    ("PSE", "Prevention secondaire"),
    ("FAR", "Fibrilation Atriale"),
    ("VAL", "Valvulopathie"),
    ("PCA", "Pontages Cardiaques"),
    ("CVA", "Chirurgie Vasculaire Arterielle"),
    ("AEP", "ATCD EP"),
    ("TVP", "ATCD TVP"),
    ("AIT", "ATCD AVC + AIT"),
    ("CMI", "CMI"),
    ("SCA", "Stents Cardiaques"),
    ("GRE", "Greffe"),
    ("TPO", "Thrombose Porte"),
    ("TME", "Thrombose Mesenterique")
)

TRAIT_CHOICES = [
    ("Aspirine", "Aspirine, Asaflow, Cardioaspirine"),
    ("Clopidogrel", "Clopidogrel, PLAVIX"),
    ("Prasugrel", "Prasugrel, EFFIENT"),
    ("Ticlopidine", "Ticlopidine, TICLID"),
    ("Dipyridamole", "Dipyridamole"),
    ("Ticagrelor", "Ticagrelor, BRILIQUE"),
    ("Acenocoumarol", "Acénocoumarol, SINTROM"),
    ("Phenprocoumone", "Phenprocoumone, MARCOUMAR"),
    ("Warfarine", "Warfarine, MAREVAN"),
    ("Apixaban", "Apixaban, ELIQUIS"),
    ("Dabigatran", "Dabigatran, PRADAXA"),
    ("Edoxaban", "Edoxaban, LIXIANA"),
    ("Rivaroxaban", "Rivaroxaban, XARELTO"),
    ("Enoxaparine", "Enoxaparine, CLEXANE"),
    ("Nadroparine", "Nadroparine, FRAXIPARINE, FRAXODI"),
    ("Tinzaparine", "Tinzaparine, INNOHEP"),
    ("Fondaparinux", "Fondaparinux, ARIXTRA"),
    ("HNF", "HNF, Héparine Sodique")
]

class Patient(models.Model):
    incl_num = models.AutoField(primary_key=True)
    height = models.FloatField('taille', null=False, blank=False)
    weight = models.FloatField('poids', null=False, blank=False)
    ddn = models.DateTimeField('Date de naissance', null=False, blank=False)
    ddi = models.DateTimeField("Date de l'intervention", null=False, blank=False)
    intervention = models.CharField('intervention', max_length=200, null=False, blank=False)
    chirurgie = models.CharField("Discipline de l'intervention", max_length=3, choices=CHIR_CHOICES, default='CCA', null=False, blank=False)
    pathologie = models.CharField("Pathologie justifiant le traitement", max_length=3, choices=PATH_CHOICES, default='PPR', null=False, blank=False)
    traitement1 = models.CharField("Premier traitement", max_length=15, choices=TRAIT_CHOICES, default='Aspirine', null=False, blank=False)
    traitement2 = models.CharField("Deuxième traitement", max_length=15, choices=[('Aucun', 'Aucun')]+TRAIT_CHOICES, default='Aucun', null=False, blank=False)

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


# @receiver(post_delete, sender=Patient)
# def submission_delete(sender, instance, **kwargs):
#     instance.image.delete(False)
