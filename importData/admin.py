from django.contrib import admin
from .models import Soura
from .models import Part
from .models import Year
from .models import Student
from .models import Grade

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'national_id', 'phone', 'next_amount', 'ahkam']
    search_fields = ['name', 'national_id']
    list_filter = ['next_amount', 'ahkam']

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