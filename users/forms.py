from django import forms
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=155, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    # password = forms.PasswordInput(rueq)
    captcha = CaptchaField()


class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=155, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    captcha = CaptchaField()
    
    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        data = self.cleaned_data["confirm_password"]
        if data == password:
            return data 
        else:
            raise ValidationError('password and confirm password are not same')
            
        
  
    
