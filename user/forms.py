# user/forms.py
# 회원가입 뚝딱 가능
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        

class SigninForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
