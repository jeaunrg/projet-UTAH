from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from patient.models import Patient
from .utils import generate_pdf, generate_bar_code
from patient.data import QUESTIONS
import os


@login_required(login_url='login')
def home_screen_view(request, *args, **kwargs):
	context = {}
	return render(request, 'personal/home.html', context)


@login_required(login_url='login')
def generate_pdf_view(request, slug, download='False'):
	patient = get_object_or_404(Patient, slug=slug)
	SERVER_URL = request.build_absolute_uri('/')
	barcode_filename = "barcode-{}".format(slug)
	num_patient = 251239853244

	context = {}
	context['SERVER_URL'] = SERVER_URL
	context['num_patient'] = num_patient
	context['barcode'] = generate_bar_code(num_patient)
	context['infos'] = {
		'Nom': patient.lastname,
		'Prénom': patient.firstname,
		'Date de naissance': patient.ddn.strftime('%d/%m/%Y'),
		'Poids': str(patient.weight) + ' kg',
		'Taille': str(patient.height) + ' cm',
		'Nom du chirurgien': patient.chirurgien,
		'Type de chirurgie': patient.chirurgie,
		'Date de la chirurgie': patient.ddi.strftime('%d/%m/%Y'),
		'Médecin qui fait la consultation': patient.consultant,
		'Date de la consultation': patient.ddconsult.strftime('%d/%m/%Y'),
	}
	context['results'] = {

	}
	return generate_pdf("personal/pdf_template.html", context, 'output.pdf', download=='True')
