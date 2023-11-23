from django.contrib import admin
from .models import Soura
from .models import Part
from .models import Year
from .models import Student
from .models import Grade

# Register your models here.
admin.site.register(Part)
admin.site.register(Soura)
admin.site.register(Year)
admin.site.register(Student)
admin.site.register(Grade)