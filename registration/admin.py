import openpyxl
from django.http import HttpResponse
from django.contrib import admin
from .models import NewStudent
from .filters import DuplicateNationalIDFilter
from .filters import DuplicateNameFilter

# Register your models here.
def export_as_excel(modeladmin, request, queryset):
    # Create an in-memory workbook
    wb = openpyxl.Workbook()
    ws = wb.active

    # Define the column headers
    columns = ['الاسم', 'ID', 'الرقم القومي', 'التليفون', 'الجزء', 'السورة', 'اول مرة']
    ws.append(columns)

    # Write data to the worksheet
    for obj in queryset:
        row = [
            obj.name,
            obj.id,
            obj.national_id,
            obj.phone,
            obj.part.title,
            obj.soura.title,
            obj.first_time,
        ]
        ws.append(row)

    # Save the workbook to an HttpResponse

    # Create the response
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="New Students.xlsx"'

    # Save the workbook to the response
    wb.save(response)

    return response

export_as_excel.short_description = "Export Selected as Excel"

class NewStudentAdmin(admin.ModelAdmin):
    list_display = ['name', "id", 'national_id', 'part', 'phone', 'soura', 'grade']
    search_fields = ['name', 'national_id']
    # list_filter = ['part']
    list_filter = [DuplicateNationalIDFilter, DuplicateNameFilter, 'part']
    actions = [export_as_excel]

admin.site.register(NewStudent, NewStudentAdmin)