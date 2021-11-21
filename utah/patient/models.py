from django.db import models
from django.utils.text import slugify
from django.conf import settings
from utah.choices import *
from django.core.validators import RegexValidator


def to_choice(data, add_empty=True):
    if isinstance(data, dict):
        choices = [(i, i) for i in data.keys()]
    else:
        choices = [(i, i) for i in data]
    if add_empty:
        choices = [('', '')] + choices
    return choices


class Patient(models.Model):
    #-------------------- PREOP -----------------#
    # patient
    hosp_num = models.CharField("n°dossier", max_length=12, default="", validators=[
        RegexValidator(regex='^.{12}$', message='Length has to be 12'),
        RegexValidator(regex='^[0-9]*$', message='Only digits accepted')])
    firstname = models.CharField('prénom', max_length=200, default="")
    lastname = models.CharField('nom', max_length=200, default="")
    height = models.IntegerField('taille')
    weight = models.IntegerField('poids')
    ddn = models.DateField('Date de naissance')

    # intervention
    ddi = models.DateField("Date de l'intervention", null=True, blank=True)
    intervention = models.CharField('intervention', max_length=200, default="", blank=True)
    chirurgien = models.CharField('chirurgien', max_length=200, default="", blank=True)
    chirurgie = models.CharField("Discipline de l'intervention", max_length=40, choices=to_choice(CHIR_CHOICES), blank=True)
    bleeding_risk = models.CharField("Risque hémorragique de la chirurgie", max_length=100, choices=to_choice(BLEEDRISK_CHOICES), blank=True)

    # consultation
    consultant = models.CharField('Medecin qui fait la consultation', max_length=200, default="", blank=True)
    ddconsult = models.DateField("Date de la consultation", auto_now_add=True, blank=True)

    # traitement
    traitements = models.JSONField(default=dict, blank=True)

    #-------------------- ALGO -----------------#
    algo = models.CharField("Algorithme suivi", max_length=40, choices=to_choice(ALGO_CHOICES), blank=True)
    algo_result = models.CharField('Résultat', max_length=400, default="", blank=True)
    algo_complete_results = models.JSONField(default=dict)


    #-------------------- POSTOP -----------------#
    schema_therap = models.CharField("Schéma thérapeutique donné au patient", max_length=40, default="Date exacte",
                                     choices=to_choice(["Date exacte", "Terminologie 'dernière prise à J-xx'", "Pas d'arrêt du traitement"]))
    aptt = models.IntegerField('APTT', null=True, blank=True)
    pt = models.IntegerField('PT', null=True, blank=True)
    inr = models.IntegerField('INR', null=True, blank=True)
    hemoglobine = models.IntegerField('Hémoglobine', null=True, blank=True)
    plaquette = models.IntegerField('Plaquettes', null=True, blank=True)
    dfg = models.IntegerField('DFG', null=True, blank=True)
    vol_sang = models.IntegerField('Volume de saignement peropératoire', null=True, blank=True)
    coag = models.CharField("Qualité de la coagulation selon le chirurgien", max_length=2, default='-5',
                            choices=to_choice(['-' + str(i) for i in range(6)] + ['+' + str(i) for i in range(5, -1, -1)]))

    #-------------------- HIDDEN -----------------#
    # hidden fields
    incl_num = models.AutoField(primary_key=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    #-------------------- A supprimer -----------------#
    pathologie = models.CharField("Pathologie justifiant le traitement", max_length=40, choices=to_choice(PATH_CHOICES), blank=True)
    traitement1 = models.CharField("Premier traitement", max_length=40, choices=to_choice(TRAIT_CHOICES), blank=True)
    traitement2 = models.CharField("Deuxième traitement", max_length=40, choices=to_choice(TRAIT_CHOICES), blank=True)

    # traitement 1
    date_derniere_prise_th1 = models.DateField('Date de dernière prise théorique (premier traitement)', null=True, blank=True)
    date_derniere_prise1 = models.DateField('Date de dernière prise pratique (premier traitement)', null=True, blank=True)
    inobservance1 = models.CharField("Inobservance (premier traitement)", max_length=40, default="Pas d'inobservance",
                                     choices=to_choice(["Pas d'inobservance", "Oubli", "Incompréhension", "Contre-ordre médical"]))
    # traitement 2
    date_derniere_prise_th2 = models.DateField('Date de dernière prise théorique (deuxième traitement)', null=True, blank=True)
    date_derniere_prise2 = models.DateField('Date de dernière prise pratique (deuxième traitement)', null=True, blank=True)
    inobservance2 = models.CharField("Inobservance (deuxième traitement)", max_length=40, default="Pas d'inobservance",
                                     choices=to_choice(["Pas d'inobservance", "Oubli", "Incompréhension", "Contre-ordre médical"]))


    def __str__(self):
        return str(self.incl_num)

    def save(self, *args, **kwargs):
        super(Patient, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify('patient') + "-" + str(self.incl_num)
            self.save()

    def get_infos(self):
        infos = {}
        for k, v in self.__dict__.items():
            if k != '_state':
                if v is None:
                    v = ""
                infos[k] = v
        return infos

    def get_age_at_intervention(self):
        return ((self.ddi - self.ddn) / 365).days

    def get_height(self):
        hm = int(self.height / 100)
        return "{0}m{1}".format(hm, int(self.height - hm * 100))

    def get_algo_result(self):
        if '\n' in self.algo_result:
            output = "Avant l'intervention:\n- " + self.algo_result.replace('\n', "\nAprès l'intervention:\n- ")
        else:
            output = self.algo_result
        output = output.replace('. ', '\n- ')
        return output

    def get_traitement_ids(self, **kwargs):
        ids = []
        for i, data in self.traitements.items():
            # categorie
            b1, b2, b3 = True, True, True
            if 'categorie' in kwargs:
                if kwargs['categorie'] not in data['categorie']:
                    b1 = False
            # pathologie
            if 'pathologie' in kwargs:
                if kwargs['pathologie'] != data['pathologie']:
                    b2 = False
             # traitement
            if 'traitement' in kwargs:
                if data['traitement'] not in kwargs['traitement'].split(' | '):
                    b3 = False
            if b1 and b2 and b3:
                ids.append(i)
        return ids

    def get_cure(self, **kwargs):
        for data in self.traitements.values():
            boolean = True
            for k, v in kwargs.items():
                if data.get(k) != v:
                    boolean = False
                    break
            if boolean:
                return True
        return False
