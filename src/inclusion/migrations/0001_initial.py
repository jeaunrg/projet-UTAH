# Generated by Django 3.2.8 on 2021-10-21 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nipp', models.CharField(max_length=20, verbose_name='n°IPP')),
                ('first_name', models.CharField(max_length=200, verbose_name='prénom')),
                ('last_name', models.CharField(max_length=200, verbose_name='nom')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='age')),
                ('gender', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], default='Homme', max_length=5, verbose_name='genre')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='poids')),
                ('height', models.FloatField(blank=True, null=True, verbose_name='taille')),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
