from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse

from inclusion.models import PatientFile
from inclusion.forms import CreatePatientFileForm, UpdatePatientFileForm
from account.models import Account


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

	context['form'] = form

	return render(request, "inclusion/create_patient_file.html", context)


def detail_patient_file_view(request, slug):

	context = {}

	patient_file = get_object_or_404(PatientFile, slug=slug)
	context['patient_file'] = patient_file

	return render(request, 'inclusion/detail_patient_file.html', context)



def edit_patient_file_view(request, slug):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("must_authenticate")

	patient_file = get_object_or_404(PatientFile, slug=slug)

	if patient_file.author != user:
		return HttpResponse('You are not the author of that post.')

	if request.POST:
		form = UpdatePatientFileForm(request.POST or None, request.FILES or None, instance=patient_file)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			patient_file = obj

	form = UpdatePatientFileForm(
			initial = {
					"title": patient_file.title,
					"body": patient_file.body,
					"image": patient_file.image,
			}
		)

	context['form'] = form
	return render(request, 'inclusion/edit_patient_file.html', context)

def get_patients_queryset(query=None):
	queryset = []
	queries = query.split(" ") # python install 2019 = [python, install, 2019]
	for q in queries:
		posts = PatientFile.objects.filter(
				Q(title__icontains=q) |
				Q(body__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))
