from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_view, name='main'), # 메인 뷰
    path('login/', views.login_view, name='login'), # 로그인
    path('about/', views.main_view, name='about'),  # 학원소개
    path('program/', views.main_view, name='program'),  # 프로그램
    path('admission/', views.main_view, name='admission'),  # 입학안내
    path('schedule/', views.main_view, name='schedule'),  # 학사일정
    path('library/', views.main_view, name='library'),  # 학습자료실
]