from django import forms
from .models import Account

class RegistrationForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'confirm password'}))
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']

        widgets = {
            'first_name': forms.TextInput(attrs={'autofocus': 'True','class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

