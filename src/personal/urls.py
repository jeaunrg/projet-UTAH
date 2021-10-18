from django.urls import path
from personal.views import (
	create_patient_file_view,
    process_view,
    home_screen_view,
)

app_name = 'personal'

urlpatterns = [
	path('process/', process_view, name='process'),
    path('include/', create_patient_file_view, name="include"),

 ]
