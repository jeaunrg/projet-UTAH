from django.urls import path
from personal.views import (
    process_view,
    generate_pdf_view,
)


app_name = 'personal'

urlpatterns = [
	path('process/', process_view, name='process'),
    path('pdf/<slug>/<download>/', generate_pdf_view, name='pdf'),

 ]
