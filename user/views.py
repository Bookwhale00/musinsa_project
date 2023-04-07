#view 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse
from .forms import SignupForm
from .forms import SigninForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth


def home(request):
    if request.user.is_authenticated:
        return redirect('/product-create')
    else:
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
            # 유효성 오류일 때 메시지
            error_msg = '올바른 패스워드를 입력해주세요.'
            return render(request, 'user/signup.html',{'form':form, 'error_msg':error_msg})
    else:
        form = SignupForm()
    return render(request, 'user/signup.html', {'form':form})

def signin(request):
    # 로그인 view
    if request.method == 'POST':
        #form = SigninForm(request.POST)
        form = SigninForm(data=request.POST)
        is_valid = form.is_valid()
        print(is_valid)
        for field in form:
            print("Field Error:", field.name,  field.errors)
        if form.is_valid():
            username = form.cleaned_data.get('username','')
            password = form.cleaned_data.get('password','')
            print('username:', username)
            print('password:', password) # 들어오는 데이터 출력 - 확인
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/product-create')
            
        else:
            print('form.errors:', form.errors) # 검증 실패한 이유 좀 알자!
            # 인증 실패 시 오류 메시지
            error_msg = '유저이름 혹은 패스워드를 확인해주세요.'
            return render(request, 'user/signin.html',{'form':form, 'error_msg':error_msg})  
    else:
        form = SigninForm()
    return render(request, 'user/signin.html', {'form':form})

def user_logout(request):
#     # 로그아웃 view
    auth_logout(request)
    return redirect('/')