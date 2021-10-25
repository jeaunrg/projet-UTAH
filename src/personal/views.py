from django.shortcuts import render, redirect
from .tasks import first_algo
from account.models import Account
from django.contrib.auth.decorators import login_required
from inclusion.models import Patient
from personal.utils import generate_pdf


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
def generate_pdf_view(request, download='True'):
	filename = 'output.pdf'
	context = {'button_name': 'Cliquez ici'}

	return generate_pdf("personal/mytemplate.html", context, filename, download=='True')
