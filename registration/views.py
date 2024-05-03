from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.http import JsonResponse
from importData.models import Student, Part, Soura
from .models import NewStudent
from .forms import NationalIDForm, SubmitNewStudentForm

# Create your views here.
form = {'nationalIDForm': NationalIDForm}
form['hideNationalID'] = False
form['nationalID'] = None
form['student'] = None
form['min_amount'] = 1

@csrf_protect
def registration(request):
    if request.method == "POST":
        if 'nationalIDForm' in request.POST:
            national_id = request.POST.get('nationalID')
            form['hideNationalID'] = True
            form['nationalID'] = national_id
            if national_id != None:
                newStudent = NewStudent.objects.filter(national_id = national_id).first()
                if newStudent is None:
                    try:
                        student = Student.objects.get(national_id = national_id)
                        form['min_amount'] = student.next_amount.number
                        form['student'] = student
                        form['form'] = SubmitNewStudentForm(initial={'national_id': form['nationalID'], 'name': student.name, 'phone': student.phone}, min_amount=form['min_amount'])
                    except:
                        form['min_amount'] = 1
                        form['student'] = None
                        form['form'] = SubmitNewStudentForm(initial={'national_id': form['nationalID']}, min_amount=form['min_amount'])
                else:
                    try:
                        student = Student.objects.get(national_id = national_id)
                        form['min_amount'] = student.next_amount.number
                        form['student'] = student
                        form['form'] = SubmitNewStudentForm(min_amount=form['min_amount'], student_id=newStudent.id)
                    except:
                        form['min_amount'] = 1
                        form['student'] = None
                        form['form'] = SubmitNewStudentForm(min_amount=form['min_amount'], student_id=newStudent.id)        
        elif 'submitForm' in request.POST:
            form['hideNationalID'] = True
            newStudent = NewStudent.objects.filter(national_id = form['nationalID']).first()
            if newStudent is None:
                form['form'] = SubmitNewStudentForm(request.POST, min_amount=form['min_amount'])
                if form['form'].is_valid():
                    submittedStudent = form['form'].save(commit=False)
                    if form['student'] is None:
                        submittedStudent.first_time = True
                    else:
                        submittedStudent.first_time = False
                    submittedStudent.save()
                    submittedStudent = SubmitNewStudentForm()
                    return HttpResponseRedirect("/?sucessSubmit=1")
            else:
                form['form'] = SubmitNewStudentForm(request.POST, min_amount=form['min_amount'], instance=newStudent)
                if form['form'].is_valid():
                    form['form'].instance.save()
                    form['form'] = SubmitNewStudentForm()
                    return HttpResponseRedirect("/?sucessSubmit=1")
    elif request.method == 'GET':
        form['hideNationalID'] = False
        form['nationalID'] = None
        form['student'] = None
    return render(request, 'registration/registration-form.html', form)

def loadSoura(request):
    data = []
    try:
        part_id = request.GET.get('part')
        part = Part.objects.get(pk=part_id)
        souras = part.soura.values('id', 'title', 'number')
        for soura in souras:
            if (int(part.number) <= 15 and int(soura['number']) >= 18) or (int(part.number) > 15 and int(soura['number']) < 18):
                data.append({'id': soura['id'], 'name': 'من سورة الناس الي سورة ' + soura['title']})
            else:
                data.append({'id': soura['id'], 'name': 'من سورة البقرة الي سورة ' + soura['title']})
    except:
        souras = Soura.objects.none()
        data = [{'id': soura['id'], 'name': soura['title']} for soura in souras]
    return JsonResponse(data, safe=False)