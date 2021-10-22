from django.urls import path
from personal.views import (
    process_view,
)

app_name = 'personal'

urlpatterns = [
	path('process/', process_view, name='process'),
 ]
