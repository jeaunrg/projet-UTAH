from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from patient.models import Patient
from .utils import generate_pdf, generate_bar_code, get_patient_hospital_num
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
	num_patient = get_patient_hospital_num(patient)

	context = {}
	context['SERVER_URL'] = SERVER_URL
	context['num_patient'] = num_patient
	context['barcode'] = generate_bar_code(num_patient)
	context['patient'] = patient
	return generate_pdf("personal/pdf_template.html", context, 'output.pdf', download=='True')
