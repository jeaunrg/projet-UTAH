from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from patient.models import Patient
from .utils import generate_pdf
from editable.questions import QUESTIONS
from editable.settings import EXCEL_FILENAME, EXCEL_ENCODING
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
	context['patient'] = patient
	return generate_pdf("personal/pdf_template.html", context, f'patient_{patient.incl_num}.pdf', download=='True')


@login_required(login_url='login')
def download_data_view(request):
	query = str(Patient.objects.all().query)
	df = pd.read_sql_query(query, connection)
	excel_file = IO()
	xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')
	df.to_excel(xlwriter, 'sheetname', encoding=EXCEL_ENCODING)
	xlwriter.save()
	xlwriter.close()
	excel_file.seek(0)
	response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
	response['Content-Disposition'] = 'attachment; filename=' + EXCEL_FILENAME
	return response
