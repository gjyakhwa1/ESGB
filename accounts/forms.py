from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class Register_form(ModelForm):
    username=forms.CharField(widget=forms.TextInput(
                attrs={'class':'form-control','placeholder':'Username'}),
                    max_length=50,required=True)
    first_name=forms.CharField(widget=forms.TextInput(
                attrs={'class':'form-control','placeholder':'First Name'}),
                    max_length=50,required=True)
    last_name=forms.CharField(widget=forms.TextInput(
                attrs={'class':'form-control','placeholder':'Last Name'}),
                    max_length=50,required=True)
    email=forms.CharField(widget=forms.EmailInput(
                attrs={'class':'form-control','placeholder':'Email'}),
                    max_length=50,required=True)
    password1=forms.CharField(widget=forms.PasswordInput(
                attrs={'class':'form-control','placeholder':'Password'}),
                    max_length=50,required=True)
    password2=forms.CharField(widget=forms.PasswordInput(
                attrs={'class':'form-control','placeholder':'Confirm Password'}),
                    max_length=50,required=True)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            match=User.objects.get(email=email)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError("Email already exists")