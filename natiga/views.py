from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from registration.models import NewStudent
from landing.forms import GetResultsForm

# Create your views here.

@csrf_exempt
def natiga(request):
    form = {'nationalIDForm': GetResultsForm}
    form['show_error'] = False
    if request.method == "POST":
        form['nationalIDForm'] = GetResultsForm(request.POST)
        if form['nationalIDForm'].is_valid():
            try:
                national_id = request.POST.get('nationalID')
                if national_id != None:
                    student = NewStudent.objects.get(national_id = national_id)
                    form['student'] = student
                    if (student.from_baqra):
                        form['soura'] = 'من سورة البقرة الي سورة ' + student.soura.title
                    else:
                        form['soura'] = student.soura.title
            except:
                form['student'] = None
                form['show_error'] = True
            form['nationalIDForm'] = GetResultsForm()
        else:
            form['nationalIDForm'] = GetResultsForm()
    return render(request, 'natiga/natiga.html', form)
