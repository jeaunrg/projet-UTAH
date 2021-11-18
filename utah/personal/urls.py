from django.urls import path
from .views import (
    generate_pdf_view,
    download_data_view,
)


app_name = 'personal'

urlpatterns = [
    path('pdf/<slug>/<download>/', generate_pdf_view, name='pdf'),
    path('data/', download_data_view, name='data'),
 ]
