from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .models import Profile, MainSlider, Philosophy, Achievement, UniversityResult, Program, Activity, SpecialSchoolResult

def main_view(request):
    # 메인 페이지에 필요한 모든 데이터를 가져옴
    context = {
        'sliders': MainSlider.objects.filter(is_active=True).order_by('order'),
        'philosophies': Philosophy.objects.filter(is_active=True).order_by('order'),
        'achievements': Achievement.objects.filter(is_active=True).order_by('-year', 'order'),
        'university_results': UniversityResult.objects.filter(is_active=True).order_by('-year', 'order'),
        'programs': Program.objects.filter(is_active=True).order_by('program_type', 'order'),
        'activities': Activity.objects.filter(is_active=True).order_by('activity_type', 'order'),
        'special_school_results': SpecialSchoolResult.objects.filter(is_active=True).order_by('-year', 'order'),
    }
    return render(request, 'main/home.html', context)

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