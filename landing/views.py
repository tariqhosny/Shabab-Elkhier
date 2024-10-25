
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseServerError

from .forms import GetResultsForm
from importData.models import Grade, Student

# Create your views here.

def landing(request):
    try:
        success = request.GET.get('sucessSubmit')
        return render(request, 'landing/landing.html', {'success': success})
    except:
        print('error')
    return render(request, 'landing/landing.html')

@csrf_exempt
def results(request):
    form = {'nationalIDForm': GetResultsForm}
    form['grades'] = []
    sour = []
    if request.method == "POST":
        form['nationalIDForm'] = GetResultsForm(request.POST)
        if form['nationalIDForm'].is_valid():
            try:
                national_id = arabic_to_english(request.POST.get('nationalID'))
                if national_id != None:
                    student = Student.objects.get(national_id = national_id)
                    grades = Grade.objects.all().filter(student = student)
                    grades = grades.reverse()
                    form['grades'] = grades
                    for grade in grades:
                        if (grade.from_baqra):
                            sour.append('من سورة الفاتحة الي سورة ' + grade.soura.title)
                        else:
                            sour.append(grade.soura.title)
                    form['sour'] = sour
            except:
                form['grades'] = None
            form['nationalIDForm'] = GetResultsForm()
    else:
        form['nationalIDForm'] = GetResultsForm()
    return render(request, 'result/result-form.html', form)


def arabic_to_english(arabic_number):
    arabic_numbers = '٠١٢٣٤٥٦٧٨٩'
    english_numbers = '0123456789'
    return arabic_number.translate(str.maketrans(arabic_numbers, english_numbers))

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