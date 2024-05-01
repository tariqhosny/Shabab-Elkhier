from django import forms
from importData.models import Soura, Part
from .models import NewStudent

class NationalIDForm(forms.Form):
    nationalID = forms.IntegerField(max_value=32412319999999, label="", widget=forms.TextInput(attrs={'placeholder': 'ادخل الرقم القومي'}))

class SubmitNewStudentForm(forms.ModelForm):
    national_id = forms.CharField(max_length=14, min_length=14, label="الرقم القومي", widget=forms.TextInput(attrs={'placeholder': 'ادخل الرقم القومي', 'disabled': True}))
    name = forms.CharField(max_length=100, label="الاسم بالكامل", widget=forms.TextInput(attrs={'placeholder': 'ادخل الاسم بالكامل'}))
    phone = forms.CharField(max_length=11, min_length=10, label="رقم التليفون", widget=forms.TextInput(attrs={'placeholder': 'ادخل رقم التليفون'}))

    class Meta:
        model = NewStudent
        fields = ['national_id', 'name', 'phone', 'part', 'soura']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['part'].label = "عدد الاجزاء"
        self.fields['soura'].label = 'السورة'
        self.fields['part'].widget.attrs.update({'id':'part', 'name':'part'})
        self.fields['soura'].widget.attrs.update({'id':'soura', 'name':'soura'})
        self.fields['soura'].queryset = Soura.objects.none()

        if 'part' in self.data:
            part_id = int(self.data.get('part'))
            part = Part.objects.get(pk=part_id)
            self.fields["soura"].queryset = part.soura.all()