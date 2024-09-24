from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .forms import UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:home')  # Redirect đến trang home sau khi login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('main:home')  # Redirect về trang login sau khi logout

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Lưu người dùng mới vào cơ sở dữ liệu
            login(request, user)  # Tự động đăng nhập sau khi đăng ký thành công
            return redirect('main:home')  # Redirect đến trang chủ sau khi đăng ký
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

