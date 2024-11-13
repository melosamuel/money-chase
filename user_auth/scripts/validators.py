from django import forms
from django.contrib.auth.hashers import make_password
import re

class RegisterForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)

    
    def clean_email(self) -> str:
        email = self.cleaned_data['email']
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if re.fullmatch(regex, email):
            return email

        raise forms.ValidationError("Not a valid Email")
    
    def clean_password(self) -> str:
        password = self.cleaned_data['password']

        return make_password(password)

    def clean_name(self) -> str:
        name = self.cleaned_data['name']
        regex = r"^[A-Za-z\s'-]{4,}$"

        if re.match(regex, name, re.UNICODE):
            return name
        
        raise forms.ValidationError("Name only allows space, ' and -. At least Name and middle name")