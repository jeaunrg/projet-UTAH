# Generated by Django 3.2.9 on 2021-11-22 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='consultant',
        ),
    ]
