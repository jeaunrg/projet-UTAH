from django.shortcuts import render, redirect, get_object_or_404
from .tasks import first_algo
from account.models import Account
from django.contrib.auth.decorators import login_required
from inclusion.models import Patient
from personal.utils import generate_pdf
from mysite.settings import STATIC_ROOT
import os


@login_required(login_url='login')
def home_screen_view(request, *args, **kwargs):
	context = {}
	return redirect("inclusion:patients", 'all')


@login_required(login_url='login')
def process_view(request):
	context = {}
	if request.method == 'POST':
		task = first_algo.delay(1)
		task_id = task.task_id
		context['task_id'] = task_id

	return render(request, 'personal/process.html', context)


@login_required(login_url='login')
def generate_pdf_view(request, slug, download='False'):
	filename = 'output.pdf'
	patient = get_object_or_404(Patient, slug=slug)
	context = patient.__dict__
	context['SERVER_URL'] = request.build_absolute_uri('/')
	return generate_pdf("personal/mytemplate.html", context, filename, download=='True')
