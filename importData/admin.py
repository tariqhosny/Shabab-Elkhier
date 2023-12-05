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
    list_filter = ['next_amount']

class GradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'year', 'grade', 'part', 'soura']
    list_filter = ['part', 'year']

class SouraAdmin(admin.ModelAdmin):
    list_display = ['title', 'number']
    search_fields = ['title', 'number']

class PartAdmin(admin.ModelAdmin):
    list_display = ['title', 'number']
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