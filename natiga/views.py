from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from importData.models import Grade, Student
from landing.forms import GetResultsForm

# Create your views here.

@csrf_exempt
def natiga(request):
    form = {'nationalIDForm': GetResultsForm}
    form['grades'] = []
    sour = []
    if request.method == "POST":
        form['nationalIDForm'] = GetResultsForm(request.POST)
        if form['nationalIDForm'].is_valid():
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
        else:
            form['nationalIDForm'] = GetResultsForm()
    return render(request, 'result/result-form.html', form)
