from django.contrib import admin
from .models import NewStudent

# Register your models here.
class NewStudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'national_id', 'phone', 'part', 'soura', 'first_time']
    search_fields = ['name', 'national_id']
    list_filter = ['first_time', 'part']
    
admin.site.register(NewStudent, NewStudentAdmin)