from django.shortcuts import render, redirect
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator




def home_screen_view(request, *args, **kwargs):

	if not request.user.is_authenticated:
		return redirect("login")

	context = {}

	return render(request, "personal/home.html", context)
