from django import forms

class GetResultsForm(forms.Form):
    nationalID = forms.CharField(max_length=14, min_length=14, label="الرقم القومي", widget=forms.TextInput(attrs={'placeholder': 'ادخل الرقم القومي'}))
    # nationalID = forms.CharField(max_length=14, label="", widget=forms.TextInput(attrs={'placeholder': 'ادخل الرقم القومي'}))
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
