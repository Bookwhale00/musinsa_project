#view 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse
from .forms import SignupForm
from .forms import SigninForm
from django.contrib import messages

def home(request):
    return redirect('/signin')

def signup(request):
    # 회원 가입 view
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/product-create')
    else:
        form = SignupForm()
    return render(request, 'user/signup.html', {'form':form})

def signin(request):
    # 로그인 view
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username','')
            password = form.cleaned_data.get('password','')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/product-create')
            
            else:
            # 인증 실패 시 오류 메시지
                error_msg = '유저이름 혹은 패스워드를 확인해주세요.'
                return render(request, 'user/signin.html',{'form':form, 'error_msg':error_msg})
       
    else:
        form = SigninForm()
    return render(request, 'user/signin.html', {'form':form})

# def user_logout(request):
#     # 로그아웃 view