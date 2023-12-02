from django import forms

class GetStudentForm(forms.Form):
    nationalID = forms.CharField(max_length=14, label="", widget=forms.TextInput(attrs={'placeholder': 'ادخل الرقم القومي'}))

