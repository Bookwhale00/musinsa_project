# user/forms.py
# 회원가입 뚝딱 가능
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length = 25,
        label = '사용자 이름',
        help_text = '사용할 사용자 이름을 입력하세요.',
    )
    password1 = forms.CharField(
        label = '비밀번호',
        help_text = '8자 이상으로 만들어주세요.',
        widget = forms.PasswordInput
    )
    password2 = forms.CharField(
        label = '비밀번호 확인',
        help_text = '비밀번호를 한번 더 입력해주세요.',
        widget = forms.PasswordInput
    )
    error_messages = {
        'password' : {
            'required': '비밀번호를 입력해주세요.',
        }
    }
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class SigninForm(forms.Form):
    pass
