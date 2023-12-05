from django.shortcuts import render
from .models import Soura
from .models import Part
from .models import Year
from .models import Student
from .models import Grade
from openpyxl import load_workbook

# Create your views here.

def importData(request):
    
    items = []

    students = Student.objects.all()
    for student in students:
        # if int(student.next_amount.number) > 7:
        #     student.ahkam = 'تحفة الأطفال ( حفظ وتطبيق )'
        # else:
        #     student.ahkam = 'لا يوجد'
        # student.save()
        item = [] 
        item.append(student.name)
        item.append(student.national_id)
        item.append(student.ahkam)
        item.append(student.next_amount.title)
        items.append(item)

    # grades = Grade.objects.all()
    # for grade in grades:
    #     if grade.student.national_id == '31011032202535': # wrong national id
    #         try:
    #             student = Student.objects.get(national_id= '31011032202525')
                # grade.student = student
                # grade.save()
            #     print('saved')
            # except (Student.DoesNotExist):
            #     print('not found')
            # student = grade.student
            # student.isFinished = True
            # student.save()
            # item = [] 
            # item.append(grade.student.name)
            # item.append(grade.student.phone)
            # item.append(grade.soura.title)
            # item.append(grade.grade)
            # item.append(grade.student.next_amount.title)
            # items.append(item)
    
    
    # excelFile = load_workbook('/Users/tariq/Desktop/2021.xlsx')
    # ws = excelFile['sheet']

    # for i in range(2, 652):
    #     phone = ws['G'+str(i)].value
    #     national_id = ws['C'+str(i)].value
        # try:
        #     student = Student.objects.get(national_id= national_id)
        #     if national_id != None and student.phone == None and phone != None:
        #         student.phone = phone
        #         student.save()
        #         item = []
        #         item.append(ws['B'+str(i)].value)
        #         item.append(ws['C'+str(i)].value)
        #         item.append(ws['G'+str(i)].value)
        #         items.append(item)
        #         print('saved')
        # except (Student.DoesNotExist):
        #     print('not found')
    return render(request, 'importData/importData.html', {'items': items})
