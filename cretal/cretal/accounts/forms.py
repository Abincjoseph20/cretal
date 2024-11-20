from django import forms
from .models import Account

class RegistrationForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password',
        'class':'form-control',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm password',
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']

    def clean(self):
        cleaned_data = super(RegistrationForms,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'password does not match!'
            )


    def __init__(self, *args, **kwargs):
        super(RegistrationForms,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='enter first name'
        self.fields['last_name'].widget.attrs['placeholder']='last name'
        self.fields['phone_number'].widget.attrs['placeholder']='phone number'
        self.fields['email'].widget.attrs['placeholder']='email'

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

