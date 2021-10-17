from django.urls import path
from personal.views import (
	create_patient_file_view,
    process_view,
    home_screen_view,
)

app_name = 'personal'

urlpatterns = [
	path('process/', process_view, name='process'),
    path('create/', create_patient_file_view, name="create"),

 ]
