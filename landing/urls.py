from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="index"),
    path('result', views.results, name="result"),
]
