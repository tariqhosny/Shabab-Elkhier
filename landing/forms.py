from django import forms

class GetResultsForm(forms.Form):
    nationalID = forms.IntegerField(max_value=32412319999999, label="", widget=forms.TextInput(attrs={'placeholder': 'ادخل الرقم القومي'}))
    # nationalID = forms.CharField(max_length=14, label="", widget=forms.TextInput(attrs={'placeholder': 'ادخل الرقم القومي'}))

