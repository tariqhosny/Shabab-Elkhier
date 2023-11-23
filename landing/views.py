from django.shortcuts import render
from .forms import GetResultsForm
from importData.models import Grade, Student

# Create your views here.

def landing(request):
    return render(request, 'landing/landing.html')

def results(request):
    form = {'form': GetResultsForm}
    try:
        national_id = request.POST.get('nationalID')
        if national_id != None:
            student = Student.objects.get(national_id = national_id)
            grades = Grade.objects.all().filter(student = student)
            form['grades'] = grades
    except:
        print("error")
    
    return render(request, 'landing/result-form.html', form)
