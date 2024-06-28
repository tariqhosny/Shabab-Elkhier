from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="index"),
    path('result', views.results, name="result"),
    path('get-csrf-token/', views.handler403, name='get_csrf_token'),
]