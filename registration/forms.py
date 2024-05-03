from django import forms
from importData.models import Soura, Part
from .models import NewStudent

class NationalIDForm(forms.Form):
    nationalID = forms.CharField(max_length=14, min_length=14, label="الرقم القومي", widget=forms.TextInput(attrs={'placeholder': 'ادخل الرقم القومي'}))

    def clean_nationalID(self):
        data = self.cleaned_data['nationalID']
        if not data.isdigit() or len(data) != 14:
            raise forms.ValidationError('لازم تدخل الرقم القومي بشكل صحيح 14 رقم')
        return data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nationalID'].error_messages = {
            'required': 'لازم تدخل الرقم القومي',
            'invalid': 'لازم تدخل الرقم القومي بشكل صحيح 14 رقم',
            'min_length': 'لازم تدخل الرقم القومي بشكل صحيح 14 رقم',
            'min_length': 'لازم تدخل الرقم القومي بشكل صحيح 14 رقم',
        }


class SubmitNewStudentForm(forms.ModelForm):
    national_id = forms.CharField(max_length=14, min_length=14, label="الرقم القومي", widget=forms.TextInput(attrs={'placeholder': 'ادخل الرقم القومي', 'disabled': True}))
    name = forms.CharField(max_length=100, label="الاسم بالكامل", widget=forms.TextInput(attrs={'placeholder': 'ادخل الاسم بالكامل'}))
    phone = forms.CharField(max_length=11, min_length=11, label="رقم التليفون", widget=forms.TextInput(attrs={'placeholder': 'ادخل رقم التليفون'}))
    checkbox = forms.BooleanField(required=True, label = 'هل انت متأكل من السورة التي قمت باختيارها؟')

    class Meta:
        model = NewStudent
        fields = ['national_id', 'name', 'phone', 'part', 'soura', 'checkbox']
    
    def __init__(self, *args, **kwargs):
        student_id = kwargs.pop('student_id', None)
        min_amount = kwargs.pop('min_amount', None)
        
        parts = Part.objects.all()
        if min_amount is not None:
            parts = Part.objects.filter(number__gte=(min_amount))
        else:
            parts = Part.objects.all()

        if student_id is not None:
            newStudent = NewStudent.objects.get(id = student_id)
            national_id = newStudent.national_id
            name = newStudent.name
            phone = newStudent.phone
            part = newStudent.part
            soura = newStudent.soura
            
        super().__init__(*args, **kwargs)

        self.fields['part'].label = "عدد الاجزاء"
        self.fields['soura'].label = 'السورة'
        self.fields['part'].widget.attrs.update({'id':'part', 'name':'part'})
        self.fields['soura'].widget.attrs.update({'id':'soura', 'name':'soura'})
        self.fields['soura'].queryset = Soura.objects.none()
        self.fields['part'].queryset = parts

        if min_amount is not None:
            if min_amount > 1:
                self.fields['name'].widget.attrs.update({'disabled': True})
            else:
                self.fields['name'].widget.attrs.update({'disabled': False})

        if student_id is not None:
            self.fields["soura"].queryset = part.soura.all()

            self.fields['national_id'].initial = national_id
            self.fields['name'].initial = name
            self.fields['phone'].initial = phone
            self.fields['part'].initial = part
            self.fields['soura'].initial = soura

        self.fields['name'].error_messages = {
            'required': 'لازم تدخل الاسم',
        }
        self.fields['phone'].error_messages = {
            'required': 'لازم تدخل رقم التليفون',
            'invalid': 'لازم ندخل رقم التليفون بشكل صحيح (01x xxx xxx xx)',
            'min_length': 'لازم ندخل رقم التليفون بشكل صحيح (01x xxx xxx xx)',
            'min_length': 'لازم ندخل رقم التليفون بشكل صحيح (01x xxx xxx xx)',
        }
        self.fields['part'].error_messages = {
            'required': 'لازم تختار عدد الاجزاء',
        }
        self.fields['soura'].error_messages = {
            'required': 'لازم تختار سورة',
        }
        self.fields['checkbox'].error_messages = {
            'required': 'لازم تختار المربع',
        }

        if 'part' in self.data:
            try:
                part_id = int(self.data.get('part'))
                part_obj = Part.objects.get(pk=part_id)
                self.fields["soura"].queryset = part_obj.soura.all()

                # souras = part_obj.soura.all()
                # for soura in souras:
                #     if (int(part_obj.number) <= 15 and int(soura.number) >= 18) or (int(part_obj.number) > 15 and int(soura.number) < 18):
                #         soura.title = 'من سورة الناس الي سورة ' + soura.title
                #     else:
                #         soura.title = 'من سورة البقرة الي سورة ' + soura.title
                # print(part_obj.soura.all())
                # self.fields['soura'].queryset = souras
            except:
                self.fields['soura'].queryset = Soura.objects.none()

    def clean_name(self):
            full_name = self.cleaned_data.get('name')
            names = full_name.split() if full_name else []

            if len(names) < 4:
                raise forms.ValidationError("لازم الاسم بالكامل يكون اسم رباعي كما هو في شهادة الميلاد")
            
            for name in names:
                if len(name) < 3:
                    raise forms.ValidationError("لازم الاسم بالكامل يكون اسم رباعي كما هو في شهادة الميلاد")

            return name
    
    def clean_phone(self):
        data = self.cleaned_data['phone']
        if not data.isdigit() or len(data) != 11:
            raise forms.ValidationError('لازم ندخل رقم التليفون بشكل صحيح (01x xxx xxx xx)')
        return data