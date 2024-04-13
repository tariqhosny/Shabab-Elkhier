from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from .forms import GetStudentForm
from importData.models import Student

# Create your views here.

@csrf_protect
def submitForm(request):
    form = {'student': False, 'form': None}
    try:
        national_id = request.POST.get('nationalID')
        if national_id != None:
            student = Student.objects.get(national_id = national_id)
            form['student'] = student
        else:
            form['form'] = GetStudentForm
            form['student'] = True
    except:
        form['form'] = GetStudentForm
        form['student'] = None
    
    return render(request, 'submitStudent/submit-form.html', form)
