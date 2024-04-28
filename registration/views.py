from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from importData.models import Grade, Student

# Create your views here.

@csrf_protect
def landing(request):
    return render(request, 'registration/registration-form.html')