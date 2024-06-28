from django.urls import path
from django.conf.urls import handler403
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.landing, name="index"),
    path('result', views.results, name="result"),
]

def custom_csrf_failure_view(request, reason=""):
    return render(request, 'errors.error.html')

handler403 = custom_csrf_failure_view
