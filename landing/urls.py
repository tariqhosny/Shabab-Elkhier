from django.urls import path
from . import views
from django.conf.urls import handler403

urlpatterns = [
    path('', views.landing, name="index"),
    path('result', views.results, name="result"),
]

handler403 = views.handler403