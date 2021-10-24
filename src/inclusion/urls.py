from django.urls import path
from inclusion.views import (
	create_patient_view,
	detail_patient_view,
	edit_patient_view,
    patients_view,
)

app_name = 'inclusion'

urlpatterns = [
    path('patients/<filter>/', patients_view, name="patients"),
    path('create/', create_patient_view, name="create"),
    path('<slug>/', detail_patient_view, name="detail"),
    path('<slug>/edit/', edit_patient_view, name="edit"),

 ]
