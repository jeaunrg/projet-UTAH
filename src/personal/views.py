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
def generate_pdf_view1(request, slug, download='False'):
	filename = 'output.pdf'
	patient = get_object_or_404(Patient, slug=slug)
	context = {'patient': patient}
	results = {}
	for k, v in patient.resultats.items():
		if k in QUESTIONS:
			results[QUESTIONS[k]['question']] = v
		else:
			results['Conclusion'] = v
	context['results1'] = results

	context['num_patient'] = 251239853244
	context['barcode'] = generate_bar_code(context['num_patient'])
	# context['informations'] = {
	# 	"Nom": "Murray",
	# 	"Prénom": "Bill",
	# 	"Date de naissance": patient.ddn,
	# 	"Poids": patient.weight,
	# 	"Taille": patient.height,
	# 	"Nom du chirurgien": patient.chirurgien,
	# 	"Type de chirurgie": patient.chirurgie,
	# 	"Date de la chirurgie": patient.ddchir,
	# 	"Nom du médecin qui fait la consultation": patient.author,
	# 	"Date de la consultation": patient.ddcons
	# }
	context['results'] = {

	}
	context['SERVER_URL'] = request.build_absolute_uri('/')
	return generate_pdf("personal/pdf_template.html", context, filename, download=='True')


@login_required(login_url='login')
def generate_pdf_view(request, slug, download='False'):
	filename = 'output.pdf'
	patient = get_object_or_404(Patient, slug=slug)
	SERVER_URL = request.build_absolute_uri('/')
	barcode_filename = "barcode-{}".format(slug)
	num_patient = 251239853244

	context = {}
	context['SERVER_URL'] = SERVER_URL
	context['num_patient'] = num_patient
	context['barcode'] = generate_bar_code(num_patient)
	context['infos'] = {
		# 'Nom': patient.name,
		# 'Prénom': patient.firstname,
		'Date de naissance': patient.ddn.strftime('%d/%m/%Y'),
		'Poids': str(patient.weight) + ' kg',
		'Taille': str(patient.height) + ' cm',
		# 'Nom du chirurgien': patient.chirurgien,
		'Type de chirurgie': patient.chirurgie,
		# 'Date de la chirurgie': patient.ddchir,
		# 'Nom du médecin qui fait la consultation': patient.consultant,
		# 'Date de la consultation': patient.ddconsult
	}
	context['results'] = {
		
	}

	return generate_pdf("personal/pdf_template.html", context, filename, download=='True')
