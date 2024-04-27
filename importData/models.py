from django.db import models

# Create your models here.

class Soura(models.Model):
    title = models.CharField(max_length=100)
    number = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.title

class Part(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    soura = models.ManyToManyField(Soura)

    def __str__(self) -> str:
        return self.title

class Year(models.Model):
    hijri_year = models.CharField(max_length=4)
    year = models.CharField(max_length=4)

    def __str__(self) -> str:
        return self.hijri_year

class Student(models.Model):
    name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, null=True, blank=True)
    next_amount = models.ForeignKey(Part, on_delete=models.PROTECT)
    ahkam = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    isFinished = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name 

class Grade(models.Model):
    grade = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    year = models.ForeignKey(Year, on_delete=models.PROTECT)
    part = models.ForeignKey(Part, on_delete=models.PROTECT)
    soura = models.ForeignKey(Soura, null=True, on_delete=models.PROTECT, related_name='student_soura')
    from_baqra = models.BooleanField(default=False)

    class Meta:
        ordering = ['student']

    def __str__(self) -> str:
        return self.student.name