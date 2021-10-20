from django.urls import path
from inclusion.views import (
	create_patient_file_view,
	detail_patient_file_view,
	edit_patient_file_view,
)

app_name = 'inclusion'

urlpatterns = [
    path('create/', create_patient_file_view, name="create"),
    path('<slug>/', detail_patient_file_view, name="detail"),
    path('<slug>/edit/', edit_patient_file_view, name="edit"),
 ]
