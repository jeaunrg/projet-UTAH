from django.urls import path
from .views import algo_view

app_name = 'algorithm'

urlpatterns = [
    path('<slug>/algo/', algo_view, name="algo"),
 ]
