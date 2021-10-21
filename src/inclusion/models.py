from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.forms import ModelForm



class Patient(models.Model):
    nipp = models.CharField('n°IPP', max_length=20, null=False, blank=False)
    first_name = models.CharField('prénom', max_length=200, null=False, blank=False)
    last_name = models.CharField('nom', max_length=200, null=False, blank=False)
    age = models.IntegerField('age', null=True, blank=True)
    gender = models.CharField('genre', max_length=5, choices=(('Homme', 'Homme'),('Femme', 'Femme')), default='Homme', null=False, blank=False)
    weight = models.FloatField('poids', null=True, blank=True)
    height = models.FloatField('taille', null=True, blank=True)

    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.nipp

    def save(self, *args, **kwargs):
        super(Patient, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify('patient') + "-" + str(self.id)
            self.save()


@receiver(post_delete, sender=Patient)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
