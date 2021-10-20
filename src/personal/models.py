from django.db import models
# from django.db.models.signals import pre_save
# from django.utils.text import slugify
# from django.conf import settings
# from django.db.models.signals import post_delete
# from django.dispatch import receiver
#
# class PatientFile(models.Model):
#     nipp = models.CharField(max_length=20)
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=1, choices=(('M', 'Homme'),('F', 'Femme')), default='M')
#     weight = models.FloatField()
#     height = models.FloatField()
#
#     date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
#     date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated")
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     slug = models.SlugField(blank=True, unique=True)
#
#     def __str__(self):
#         return self.nipp
#
#
# def pre_save_patient_file_receiver(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = slugify(instance.author.username + "-" + instance.nipp)
#
# pre_save.connect(pre_save_patient_file_receiver, sender=PatientFile)
