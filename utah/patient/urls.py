from django.urls import path
from .views import (
    select_patient_view,
    preop_patient_view,
    postop_patient_view,
    detail_patient_view,
    edit_patient_view,
    patients_view,
    add_traitement_view,
    edit_traitement_view,
)

app_name = 'patient'

urlpatterns = [
    path('select/<op>/', select_patient_view, name="select"),
    path('patients/<filter>/', patients_view, name="patients"),
    path('preop/', preop_patient_view, name="preop"),
    path('postop/<slug>/', postop_patient_view, name="postop"),
    path('<slug>/', detail_patient_view, name="detail"),
    path('<slug>/edit/', edit_patient_view, name="edit"),
    path('<slug>/addtrt/', add_traitement_view, name="addtrt"),
    path('<slug>/<idtrt>/edittrt/', edit_traitement_view, name="edittrt"),
]
