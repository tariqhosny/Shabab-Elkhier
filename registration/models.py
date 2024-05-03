from django.db import models
from importData.models import Soura
from importData.models import Part

# Create your models here.

class NewStudent(models.Model):
    name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=14)
    phone = models.CharField(max_length=20)
    part = models.ForeignKey(Part, on_delete=models.PROTECT)
    soura = models.ForeignKey(Soura, on_delete=models.PROTECT, related_name='new_student_soura')
    new_student = models.BooleanField(default=False)
