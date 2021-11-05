# Generated by Django 3.2.9 on 2021-11-03 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_auto_20211103_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='coag',
            field=models.CharField(blank=True, choices=[('-0', '-0'), ('-1', '-1'), ('-2', '-2'), ('-3', '-3'), ('-4', '-4'), ('-5', '-5'), ('+5', '+5'), ('+4', '+4'), ('+3', '+3'), ('+2', '+2'), ('+1', '+1'), ('+0', '+0')], default='-5', max_length=2, verbose_name='Qualité de la coagulation selon le chirurgien'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='chirurgie',
            field=models.CharField(choices=[('Chirurgie Cardiaque', 'Chirurgie Cardiaque'), ('Chirurgie Digestive', 'Chirurgie Digestive'), ('Chirurgie Gynecologique', 'Chirurgie Gynecologique'), ('Chirurgie Hepatique', 'Chirurgie Hepatique'), ('Chirurgie Orthopedique', 'Chirurgie Orthopedique'), ('Chirurgie Ophtalmologique', 'Chirurgie Ophtalmologique'), ('Chirurgie Plastique', 'Chirurgie Plastique'), ('Chirurgie Thoracique', 'Chirurgie Thoracique'), ('Chirurgie Urologique', 'Chirurgie Urologique'), ('Endoscopie', 'Endoscopie'), ('Neurochirurgie', 'Neurochirurgie'), ('Chirurgie ORL', 'Chirurgie ORL'), ('Radiologie Interventionnelle', 'Radiologie Interventionnelle'), ('Stomatologie', 'Stomatologie')], default='Chirurgie Cardiaque', max_length=40, verbose_name="Discipline de l'intervention"),
        ),
    ]
