from django.shortcuts import render
from .models import Soura
from .models import Part
from .models import Year
from .models import Student
from .models import Grade
from openpyxl import load_workbook

# Create your views here.

def importData(request):
    
    # counter = 0
    items = []

    # grades = Grade.objects.all()
    # parts = Part.objects.all()
    # for grade in grades:
    #     if grade.year.hijri_year == "1444":
    #         if int(grade.part.number) > 0 and int(grade.part.number) <= 3:
    #             next_amount = Part.objects.get(number = str(int(grade.part.number) + 1))
    #         elif int(grade.part.number) >= 4 and int(grade.part.number) <= 8:
    #             next_amount = Part.objects.get(number = str(int(grade.part.number) + 2))
    #         elif int(grade.part.number) >= 9 and int(grade.part.number) <= 15:
    #             next_amount = Part.objects.get(number = str(int(grade.part.number) + 3))
    #         elif int(grade.part.number) >= 16 and int(grade.part.number) <= 20:
    #             next_amount = Part.objects.get(number = str(int(grade.part.number) + 4))
    #         elif int(grade.part.number) >= 20 and int(grade.part.number) <= 25:
    #             next_amount = Part.objects.get(number = str(int(grade.part.number) + 5))
    #         else:
    #             next_amount = Part.objects.get(number = 30)
    #         # student = grade.student
    #         # student.next_amount = next_amount 
    #         # student.save()
    #         print("Saved")
    #         item = [] 
    #         item.append(grade.student.name)
    #         item.append(grade.year.hijri_year)
    #         item.append(grade.part.number)
    #         item.append(grade.part.soura.first().title)
    #         items.append(item)
    
    
    # excelFile = load_workbook('/Users/tariq/Desktop/2021.xlsx')
    # ws = excelFile['sheet']

    # for i in range(2, 852):
        # for j in range(0, 3):
        #     student = Student.objects.get(national_id= ws['C'+str(i)].value)
        #     if j == 0:
        #         part = Part.objects.get(number= ws['D'+str(i)].value)
        #         grade = ws['J'+str(i)].value
        #         year = Year.objects.get(year= '2021')
        #     elif j == 1:
        #         part = Part.objects.get(number= ws['E'+str(i)].value)
        #         grade = ws['K'+str(i)].value
        #         year = Year.objects.get(year= '2022')
        #     else:
                # part = Part.objects.get(number= ws['F'+str(i)].value)
                # grade = ws['L'+str(i)].value
                # year = Year.objects.get(year= '2023')

            # data = Grade(grade= grade, student= student, part= part, year= year)
            # data.save()
        # name = ws['A'+str(i)].value
        # phone = ws['F'+str(i)].value
        # national_id = ws['B'+str(i)].value
        # try:
        #     student = Student.objects.get(national_id= national_id)
        #     if national_id != None:
        #         part = Part.objects.get(number= ws['E'+str(i)].value)
        #         grade = ws['C'+str(i)].value
        #         year = Year.objects.get(year= '2021')
        #         soura = part.soura.first()
        #         data = Grade(grade= grade, student= student, part= part, year= year, soura= soura)
        #         # data.save()
        #         counter = counter + 1
        # except (Student.DoesNotExist):
        #     print('tariq')
        # item = []
        # item.append(ws['A'+str(i)].value)
        # item.append(ws['B'+str(i)].value)
        # items.append(item)
    # print(counter)
    return render(request, 'importData/importData.html', {'items': items})
