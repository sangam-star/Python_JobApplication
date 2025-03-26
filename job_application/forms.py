## not fix

from django import forms

#class JobApplicationForm(forms.Form): not fix
class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    occupation = forms.CharField(max_length=100)