from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from patient.models import Patient
from .utils import generate_pdf
from patient.data import QUESTIONS


@login_required(login_url='login')
def home_screen_view(request, *args, **kwargs):
	context = {}
	return render(request, 'personal/home.html', context)


@login_required(login_url='login')
def generate_pdf_view(request, slug, download='False'):
	filename = 'output.pdf'
	patient = get_object_or_404(Patient, slug=slug)
	context = {'patient': patient}
	results = {}
	for k, v in patient.resultats.items():
		if k in QUESTIONS:
			results[QUESTIONS[k]['question']] = v
		else:
			results['Conclusion'] = v
	context['results'] = results
	context['SERVER_URL'] = request.build_absolute_uri('/')
	return generate_pdf("personal/mytemplate.html", context, filename, download=='True')
