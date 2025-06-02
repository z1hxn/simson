from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .models import Profile

def main_view(request):
    return render(request, 'main/home.html')  # main.html로 수정

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            try:
                role = user.profile.role
            except Profile.DoesNotExist:
                messages.error(request, '프로필이 존재하지 않습니다.')
                return redirect('login')

            if role == 'student':
                return render(request, 'student.html')
            elif role == 'teacher':
                return render(request, 'teacher.html')
            elif role == 'admin':
                return redirect(reverse('admin:index'))
            else:
                messages.error(request, '정의되지 않은 사용자 유형입니다.')
                return redirect('login')
        else:
            return render(request, 'main/login.html', {
                'error': '아이디 또는 비밀번호가 올바르지 않습니다.'
            })

    return render(request, 'main/login.html')