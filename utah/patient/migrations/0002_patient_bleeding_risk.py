# Generated by Django 3.2.9 on 2021-11-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='bleeding_risk',
            field=models.CharField(blank=True, choices=[('', ''), ('faible', 'faible'), ('intermédiaire', 'intermédiaire'), ('élevé', 'élevé')], max_length=100, verbose_name='Risque hémorragique de la chirurgie'),
        ),
    ]
