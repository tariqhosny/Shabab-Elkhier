from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from .forms import GetResultsForm
from importData.models import Grade, Student

# Create your views here.

@csrf_protect
def landing(request):
    try:
        success = request.GET.get('sucessSubmit')
        print(success)
        return render(request, 'landing/landing.html', {'success': success})
    except:
        print('error')
    return render(request, 'landing/landing.html')

@csrf_protect
def results(request):
    form = {'form': GetResultsForm}
    form['grades'] = []
    sour = []
    try:
        national_id = request.POST.get('nationalID')
        if national_id != None:
            student = Student.objects.get(national_id = national_id)
            grades = Grade.objects.all().filter(student = student)
            form['grades'] = grades
            for grade in grades:
                if (grade.from_baqra):
                    sour.append('من سورة الفاتحة الي سورة ' + grade.soura.title)
                else:
                    sour.append(grade.soura.title)
            form['sour'] = sour
    except:
        form['grades'] = None
        print("error")
    
    return render(request, 'landing/result-form.html', form)
