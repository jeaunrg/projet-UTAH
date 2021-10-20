from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import AccountAuthenticationForm, AccountUpdateForm
from django.contrib.auth.decorators import login_required
from inclusion.models import PatientFile

def logout_view(request):
	logout(request)
	return redirect('/')


def login_view(request):

	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user:
				login(request, user)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)


@login_required(login_url='login')
def account_view(request):

	context = {}
	if request.POST:
		last_picture = request.user.profile_picture
		if last_picture:
			last_picture_url = last_picture.url
		else:
			last_picture_url = None

		form = AccountUpdateForm(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			account = form.save(commit=False)
			account.save()
			print("SAVE")

			form.initial = {
					"username": request.POST['username'],
					"email": request.POST['email'],
			}
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm(
			initial={
					"username": request.user.username,
					"email": request.user.email,
				}
			)

	context['account_form'] = form

	patient_files = PatientFile.objects.filter(author=request.user)
	context['patient_files'] = patient_files

	return render(request, "account/account.html", context)
