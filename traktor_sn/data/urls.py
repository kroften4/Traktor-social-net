from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_home, name='data_home'),
    path('create', views.create, name='create')
]