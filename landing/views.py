from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseServerError

from .forms import GetResultsForm
from importData.models import Grade, Student

# Create your views here.

@csrf_protect
def landing(request):
    try:
        success = request.GET.get('sucessSubmit')
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


#error handling
def handler400(request, *args, **argv):
    # return render(request, "errors/error.html", {'code': 400})
    return HttpResponseBadRequest(render(request, "errors/error.html", {'code': 400}))

def handler403(request, *args, **argv):
    # return render(request, "errors/error.html", {'code': 403})
    return HttpResponseForbidden(render(request, "errors/error.html", {'code': 403}))

def handler404(request, *args, **argv):
    # return render(request, "errors/error.html", {'code': 404})
    return HttpResponseNotFound(render(request, "errors/error.html", {'code': 404}))

def handler500(request, *args, **argv):
    # return render(request, "errors/error.html", {'code': 500})
    return HttpResponseServerError(render(request, "errors/error.html", {'code': 500}))