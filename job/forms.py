from django import forms

from .models import Application, Job

class ApplicationForm(forms.ModelForm):
    
    class Meta:
        model = Application
        fields = ['name','email', 'website', 'cv', 'cover_letteer']



class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug','owner',)