from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class Myblog(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','blog']
        widget={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'blog':forms.Textarea(attrs={'rows':5,'col':25,'class':'form-control'})
        }

class sign(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=['username','first_name', 'last_name','email']
        label={'email':'Enter Email'}

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

