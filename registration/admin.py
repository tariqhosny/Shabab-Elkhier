from django.contrib import admin
from .models import NewStudent

# Register your models here.
class NewStudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'national_id', 'phone', 'part', 'soura', 'new_student']
    search_fields = ['name', 'national_id']
    list_filter = ['part', 'soura']
    
admin.site.register(NewStudent, NewStudentAdmin)