from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from importData.models import Student, Part, Soura
from .models import NewStudent
from .forms import NationalIDForm, SubmitNewStudentForm

# Create your views here.
form = {'hideNationalID': False}
# form['hideNationalID'] = False
form['nationalID'] = None
form['student'] = None
form['min_amount'] = 1

@csrf_exempt
def registration(request):
    form['nationalIDForm'] = NationalIDForm()
    if request.method == "POST":
        if 'nationalIDForm' in request.POST:
            form['nationalIDForm'] = NationalIDForm(request.POST)
            if form['nationalIDForm'].is_valid():
                national_id = arabic_to_english(request.POST.get('nationalID'))
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
                    phone = arabic_to_english(form['form'].cleaned_data.get('phone'))
                    submittedStudent.phone = phone
                    if form['student'] is None:
                        submittedStudent.first_time = True
                    else:
                        submittedStudent.first_time = False
                    form['form'].save()
                    form['form'] = SubmitNewStudentForm()
                    return HttpResponseRedirect("/?sucessSubmit=1")
            else:
                form['form'] = SubmitNewStudentForm(request.POST, min_amount=form['min_amount'], instance=newStudent)
                if form['form'].is_valid():
                    submittedStudent = form['form'].save(commit=False)
                    phone = arabic_to_english(form['form'].cleaned_data.get('phone'))
                    submittedStudent.phone = phone
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

def arabic_to_english(arabic_number):
    arabic_numbers = '٠١٢٣٤٥٦٧٨٩'
    english_numbers = '0123456789'
    return arabic_number.translate(str.maketrans(arabic_numbers, english_numbers))
