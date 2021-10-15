from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator




def home_screen_view(request, *args, **kwargs):

	context = {}

	return render(request, "personal/home.html", context)
