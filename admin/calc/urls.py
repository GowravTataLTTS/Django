from django.urls import path
# Importing the views
from . import views

urlpatterns = [
    path('', views.home, name='home')
]
