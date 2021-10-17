from django.shortcuts import render, redirect
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .tasks import first_algo
from .forms import CreatePatientFileForm
from account.models import Account


def home_screen_view(request, *args, **kwargs):

	if not request.user.is_authenticated:
		return redirect("login")

	context = {}

	return render(request, "personal/home.html", context)


def create_patient_file_view(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

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

# def include_view(request):
# 	context = {}
# 	if request.method == 'POST':
# 		form = PatientFileForm(request.POST)
# 		if form.is_valid():
# 			context['success_message'] = "Patient inclus !"
# 	else:
# 		form = PatientFileForm()
#
# 	context['form'] = form
# 	return render(request, 'personal/include.html', context)


def process_view(request):
	context = {}
	if request.method == 'POST':
		task = first_algo.delay(1)
		task_id = task.task_id
		context['task_id'] = task_id

	return render(request, 'personal/process.html', context)
