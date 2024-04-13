from django import forms

class GetResultsForm(forms.Form):
    nationalID = forms.CharField(max_length=14, label="", widget=forms.TextInput(attrs={'placeholder': 'ادخل الرقم القومي'}))

