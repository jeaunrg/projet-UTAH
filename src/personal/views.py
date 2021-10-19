from django.shortcuts import render, redirect
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .tasks import first_algo
from .forms import CreatePatientFileForm
from account.models import Account
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home_screen_view(request, *args, **kwargs):
	context = {}
	return render(request, "personal/home.html", context)


@login_required(login_url='login')
def create_patient_file_view(request):

	context = {}

	user = request.user

	form = CreatePatientFileForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(username=user.username).first()
		obj.author = author
		obj.save()
		form = CreatePatientFileForm()
		context['success_message'] = "Patient inclus !"

	context['form'] = form

	return render(request, "personal/create_patient_file.html", context)


@login_required(login_url='login')
def process_view(request):
	context = {}
	if request.method == 'POST':
		task = first_algo.delay(1)
		task_id = task.task_id
		context['task_id'] = task_id

	return render(request, 'personal/process.html', context)
