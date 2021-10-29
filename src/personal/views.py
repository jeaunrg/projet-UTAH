from django.shortcuts import render, redirect, get_object_or_404
from account.models import Account
from django.contrib.auth.decorators import login_required
from patient.models import Patient
from personal.utils import generate_pdf
from mysite.settings import STATIC_ROOT
import os


@login_required(login_url='login')
def home_screen_view(request, *args, **kwargs):
	context = {}
	return render(request, 'personal/home.html', context)


	# return redirect("patient:patients", 'all')

@login_required(login_url='login')
def generate_pdf_view(request, slug, download='False'):
	filename = 'output.pdf'
	patient = get_object_or_404(Patient, slug=slug)
	context = patient.getInfos()
	context['SERVER_URL'] = request.build_absolute_uri('/')
	return generate_pdf("personal/mytemplate.html", context, filename, download=='True')
