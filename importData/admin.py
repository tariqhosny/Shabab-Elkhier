import openpyxl
from django.http import HttpResponse
from django.contrib import admin
from .models import Soura
from .models import Part
from .models import Year
from .models import Student
from .models import Grade

# Register your models here.
def export_as_excel(modeladmin, request, queryset):
    # Create an in-memory workbook
    wb = openpyxl.Workbook()
    ws = wb.active

    # Define the column headers
    columns = ['الاسم', 'المقرر القادم', 'الاحكام']
    ws.append(columns)

    # Write data to the worksheet
    for obj in queryset:
        row = [
            obj.name,
            obj.next_amount.number,
            obj.ahkam,
        ]
        ws.append(row)

    # Save the workbook to an HttpResponse

    # Create the response
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="All Students.xlsx"'

    # Save the workbook to the response
    wb.save(response)

    return response

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'national_id', 'phone', 'last_part', 'last_grade', 'last_soura', 'next_amount', 'ahkam']
    search_fields = ['name', 'national_id']
    list_filter = ['next_amount', 'last_part', 'isExamine']
    actions = [export_as_excel]

class GradeAdmin(admin.ModelAdmin):
    def student_national_id(self, obj):
        return obj.student.national_id if obj.student else None
    student_national_id.short_description = 'National Id'

    list_display = ['student', 'student_national_id', 'year', 'grade', 'part', 'soura', 'from_baqra']
    search_fields = ['student__name', 'student__national_id']
    list_filter = ['part', 'year', 'from_baqra']

class SouraAdmin(admin.ModelAdmin):
    list_display = ['title', 'number']
    search_fields = ['title', 'number']

class PartAdmin(admin.ModelAdmin):
    def part_soura(self, obj):
        return '  -   '.join(str(Soura) for Soura in obj.soura.all())
    part_soura.short_description = 'Soura'  # Optional: Customize column header

    list_display = ['title', 'number', 'part_soura']
    search_fields = ['title', 'number']

class YearAdmin(admin.ModelAdmin):
    list_display = ['hijri_year', 'year']
    search_fields = ['hijri_year', 'year']

admin.site.register(Part, PartAdmin)
admin.site.register(Soura, SouraAdmin)
admin.site.register(Year, YearAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.site_header = 'Shaba-Elkhier'
admin.site.site_title = 'Shaba-Elkhier'