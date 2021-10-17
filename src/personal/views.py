from django.shortcuts import render, redirect
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def home_screen_view(request, *args, **kwargs):

	if not request.user.is_authenticated:
		return redirect("login")

	context = {}

	return render(request, "personal/home.html", context)

from .tasks import go_to_sleep


def process_view(request):
	# If method is POST, process form data and start task
	if request.method == 'POST':
		# Create Task
		task = go_to_sleep.delay(1)
		# Get ID
		task_id = task.task_id
		# Print Task ID
		print(f'Celery Task ID: {task_id}')
		# Return demo view with Task ID
		return render(request, 'personal/process.html', {'task_id': task_id})
	else:
		# Return demo view
		return render(request, 'personal/process.html', {})
