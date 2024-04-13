from django import forms
from importData.models import Part

class GetStudentForm(forms.Form):
    nationalID = forms.CharField(max_length=14, label="", widget=forms.TextInput(attrs={'placeholder': 'ادخل الرقم القومي'}))

class addOldStudentForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['title', 'number', 'soura']
        labels = {
            'assessment_stage': ('Change Assessment Stage'),
        }