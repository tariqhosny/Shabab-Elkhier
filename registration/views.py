from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import JsonResponse
from importData.models import Student, Part
from .forms import NationalIDForm, SubmitNewStudentForm

# Create your views here.
form = {'nationalIDForm': NationalIDForm}
form['hideNationalID'] = False
form['nationalID'] = None
form['student'] = None

@csrf_protect
def registration(request):
    if request.method == "POST":
        if 'nationalIDForm' in request.POST:
            national_id = request.POST.get('nationalID')
            form['hideNationalID'] = True
            form['nationalID'] = national_id
            if national_id != None:
                try:
                    student = Student.objects.get(national_id = national_id)
                    form['student'] = student
                    form['form'] = SubmitNewStudentForm(initial={'national_id': form['nationalID'], 'name': student.name, 'phone': student.phone})
                except:
                    form['student'] = None
                    form['form'] = SubmitNewStudentForm(initial={'national_id': form['nationalID']})
        elif 'submitForm' in request.POST:
            form['hideNationalID'] = True
            submitForm = SubmitNewStudentForm(request.POST)
            form['form'] = submitForm
            if submitForm.is_valid():
                submitForm.save()
    elif request.method == 'GET':
        form['hideNationalID'] = False
        form['nationalID'] = None
        form['student'] = None
    return render(request, 'registration/registration-form.html', form)

def loadSoura(request):
    part_id = request.GET.get('part')
    part = Part.objects.get(pk=part_id)
    souras = part.soura.values('id', 'title')
    data = [{'id': soura['id'], 'name': soura['title']} for soura in souras]
    return JsonResponse(data, safe=False)