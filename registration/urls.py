from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name="registration"),
    path('ajax/load-soura/', views.loadSoura, name='ajax_load_soura'), 
]