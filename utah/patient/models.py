from django.db import models
from django.utils.text import slugify
from django.conf import settings
from jsonfield import JSONField
from utah.choices import CHIR_CHOICES, PATH_CHOICES, TRAIT_CHOICES, ALGO_CHOICES


def to_choice(data):
    if isinstance(data, dict):
        return [('', '')] + [(i, i) for i in data.keys()]
    else:
        return [('', '')] + [(i, i) for i in data]


class Patient(models.Model):
    #-------------------- PREOP -----------------#
    # patient
    firstname = models.CharField('prénom', max_length=200, default="")
    lastname = models.CharField('nom', max_length=200, default="")
    height = models.IntegerField('taille')
    weight = models.IntegerField('poids')
    ddn = models.DateTimeField('Date de naissance')

    # intervention
    ddi = models.DateTimeField("Date de l'intervention", null=True, blank=True)
    intervention = models.CharField('intervention', max_length=200, default="", blank=True)
    chirurgien = models.CharField('chirurgien', max_length=200, default="", blank=True)
    chirurgie = models.CharField("Discipline de l'intervention", max_length=40, choices=to_choice(CHIR_CHOICES), blank=True)

    # consultation
    consultant = models.CharField('Medecin qui fait la consultation', max_length=200, default="", blank=True)
    ddconsult = models.DateTimeField("Date de la consultation", auto_now_add=True, blank=True)

    # traitement
    pathologie = models.CharField("Pathologie justifiant le traitement", max_length=40, choices=to_choice(PATH_CHOICES), blank=True)
    traitement1 = models.CharField("Premier traitement", max_length=40, choices=to_choice(TRAIT_CHOICES), blank=True)
    traitement2 = models.CharField("Deuxième traitement", max_length=40, choices=to_choice(TRAIT_CHOICES), blank=True)

    #-------------------- ALGO -----------------#
    algo = models.CharField("Algorithme suivi", max_length=40, choices=to_choice(ALGO_CHOICES), blank=True)
    algo_result = models.CharField('Résultat', max_length=400, default="", blank=True)
    algo_complete_results = JSONField(default=dict)


    #-------------------- POSTOP -----------------#
    schema_therap = models.CharField("Schéma thérapeutique donné au patient", max_length=40, default="Date exacte",
                                     choices=to_choice(["Date exacte", "Terminologie 'dernière prise à J-xx'", "Pas d'arrêt du traitement"]))
    # traitement 1
    date_derniere_prise_th1 = models.DateTimeField('Date de dernière prise théorique (premier traitement)', null=True, blank=True)
    date_derniere_prise1 = models.DateTimeField('Date de dernière prise pratique (premier traitement)', null=True, blank=True)
    inobservance1 = models.CharField("Inobservance (premier traitement)", max_length=40, default="Pas d'inobservance",
                                     choices=to_choice(["Pas d'inobservance", "Oubli", "Incompréhension", "Contre-ordre médical"]))
    # traitement 2
    date_derniere_prise_th2 = models.DateTimeField('Date de dernière prise théorique (deuxième traitement)', null=True, blank=True)
    date_derniere_prise2 = models.DateTimeField('Date de dernière prise pratique (deuxième traitement)', null=True, blank=True)
    inobservance2 = models.CharField("Inobservance (deuxième traitement)", max_length=40, default="Pas d'inobservance",
                                     choices=to_choice(["Pas d'inobservance", "Oubli", "Incompréhension", "Contre-ordre médical"]))

    aptt = models.IntegerField('APTT', null=True, blank=True)
    pt = models.IntegerField('PT', null=True, blank=True)
    inr = models.IntegerField('INR', null=True, blank=True)
    hemoglobine = models.IntegerField('Hémoglobine', null=True, blank=True)
    plaquette = models.IntegerField('Plaquettes', null=True, blank=True)
    dfg = models.IntegerField('DFG', null=True, blank=True)
    vol_sang = models.IntegerField('Volume de saignement peropératoire', null=True, blank=True)
    coag = models.CharField("Qualité de la coagulation selon le chirurgien", max_length=2, default='-5',
                            choices=to_choice(['-' + str(i) for i in range(6)] + ['+' + str(i) for i in range(5, -1, -1)]))

    # hidden fields
    incl_num = models.AutoField(primary_key=True)
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

    def categorie1(self):
        if self.traitement1 in TRAIT_CHOICES:
            return TRAIT_CHOICES.get(self.traitement1).split('-')[0]

    def categorie2(self):
        if self.traitement2 in TRAIT_CHOICES:
            return TRAIT_CHOICES.get(self.traitement2).split('-')[0]

    def get_infos(self):
        infos = {}
        for k, v in self.__dict__.items():
            if k != '_state':
                if v is None:
                    v = ""
                infos[k] = v
        return infos

    def get_algo_result(self):
        if '\n' in self.algo_result:
            output = "Avant l'intervention:\n- " + self.algo_result.replace('\n', "\nAprès l'intervention:\n- ")
        else:
            output = self.algo_result
        output = output.replace('. ', '\n- ')
        return output

    def get_serializable_infos(self):
        return {k: v for k, v in self.__dict__.items() if isinstance(v, (str, int, float, bool))}
