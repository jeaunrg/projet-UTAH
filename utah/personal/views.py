from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from patient.models import Patient
from .utils import generate_pdf, generate_bar_code
from algorithm.questions import QUESTIONS
import os
from django.db import connection
import pandas as pd
from io import BytesIO as IO

@login_required(login_url='login')
def home_screen_view(request, *args, **kwargs):
	context = {}
	return render(request, 'personal/home.html', context)


@login_required(login_url='login')
def generate_pdf_view(request, slug, download='False'):
	patient = get_object_or_404(Patient, slug=slug)
	SERVER_URL = request.build_absolute_uri('/')

	context = {}
	context['SERVER_URL'] = SERVER_URL
	context['barcode'] = generate_bar_code(patient.hosp_num)
	context['patient'] = patient
	return generate_pdf("personal/pdf_template.html", context, 'patient_{}.pdf'.format(patient.incl_num), download=='True')


@login_required(login_url='login')
def download_data_view(request):
	query = str(Patient.objects.all().query)
	df = pd.read_sql_query(query, connection)
	excel_file = IO()
	xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')
	df.to_excel(xlwriter, 'sheetname')
	xlwriter.save()
	xlwriter.close()
	excel_file.seek(0)
	response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
	response['Content-Disposition'] = 'attachment; filename=data.xlsx'
	return response
