from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_info, name='staff-info')
]
