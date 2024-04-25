from django.shortcuts import render
from django.http import HttpResponse
from .models import Soura
from .models import Part
from .models import Year
from .models import Student
from .models import Grade
from openpyxl import Workbook

# Create your views here.

def importData(request):
    # Fetch data from the database
    # data = Student.objects.all()

    # # Create a new Excel workbook
    # wb = Workbook()
    # ws = wb.active

    # # Add column headers
    # ws.append(['الاسم', 'الرقم القومي', 'التليفون', 'المقرر', 'الاحكام'])  # Replace with actual column names

    # # Add data rows
    # for row in data:
    #     ws.append([row.name, row.national_id, row.phone, row.next_amount.title, row.ahkam])  # Replace field1, field2, field3 with actual field names

    # # Create the response
    # response = HttpResponse(content_type='application/ms-excel')
    # response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

    # # Save the workbook to the response
    # wb.save(response)

    # return response
    items = []

    # grades = Grade.objects.all()
    # for grade in grades:
    #     if grade.student.national_id == '30310012209588' or grade.student.national_id == '30005012202485':
    #         item = [] 
    #         item.append(grade.student.name)
    #         item.append(grade.part.title)
    #         item.append(grade.soura.title)
    #         if (int(grade.part.number) <= 15 and int(grade.soura.number) >= 18) or (int(grade.part.number) > 15 and int(grade.soura.number) < 18):
    #             item.append('من سورة الناس الي سورة ' + grade.soura.title)
    #         else:
    #             item.append('من سورة الفاتحة الي سورة ' + grade.soura.title)
    #         items.append(item)

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
