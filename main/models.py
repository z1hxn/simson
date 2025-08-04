# admin.py

from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', '학생'),
        ('teacher', '교사'),
        ('admin', '관리자'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    def __str__(self):
        return f"{self.user.username} ({self.role})"


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_link', 'role')
    list_display_links = ('user_link',)  # 링크 클릭 시 이동할 필드

    def user_link(self, obj):
        url = reverse('admin:auth_user_change', args=[obj.user.id])
        return format_html('<a href="{}">{}</a>', url, obj.user.username)
    
    user_link.short_description = 'User'


# 메인 페이지 콘텐츠 관리 모델들
class MainSlider(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    subtitle = models.CharField(max_length=300, verbose_name='부제목', blank=True)
    image = models.ImageField(upload_to='slider/', verbose_name='이미지', blank=True, null=True)
    order = models.IntegerField(default=0, verbose_name='순서')
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    
    class Meta:
        ordering = ['order']
        verbose_name = '메인 슬라이더'
        verbose_name_plural = '메인 슬라이더'
    
    def __str__(self):
        return self.title


class Philosophy(models.Model):
    icon = models.CharField(max_length=10, verbose_name='아이콘 (이모지)')
    title = models.CharField(max_length=100, verbose_name='제목')
    description = models.TextField(verbose_name='설명')
    order = models.IntegerField(default=0, verbose_name='순서')
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    
    class Meta:
        ordering = ['order']
        verbose_name = '교육신념'
        verbose_name_plural = '교육신념'
    
    def __str__(self):
        return self.title


class Achievement(models.Model):
    year = models.IntegerField(verbose_name='년도')
    title = models.CharField(max_length=200, verbose_name='제목')
    description = models.TextField(verbose_name='설명', blank=True)
    is_highlight = models.BooleanField(default=False, verbose_name='하이라이트 표시')
    order = models.IntegerField(default=0, verbose_name='순서')
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    
    class Meta:
        ordering = ['-year', 'order']
        verbose_name = '성과'
        verbose_name_plural = '성과'
    
    def __str__(self):
        return f"{self.year}년 - {self.title}"


class UniversityResult(models.Model):
    university = models.CharField(max_length=100, verbose_name='대학교')
    department = models.CharField(max_length=100, verbose_name='학과')
    student_name = models.CharField(max_length=50, verbose_name='학생 이름')
    high_school = models.CharField(max_length=100, verbose_name='고등학교')
    branch = models.CharField(max_length=50, verbose_name='지점', blank=True)
    year = models.IntegerField(verbose_name='합격년도')
    order = models.IntegerField(default=0, verbose_name='순서')
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    
    class Meta:
        ordering = ['-year', 'order']
        verbose_name = '대학 합격자'
        verbose_name_plural = '대학 합격자'
    
    def __str__(self):
        return f"{self.university} {self.department} - {self.student_name}"


class Program(models.Model):
    PROGRAM_TYPES = (
        ('news', 'News & Debate'),
        ('middle', '중등 내신 자료'),
        ('high', '고등 내신 자료'),
    )
    
    program_type = models.CharField(max_length=20, choices=PROGRAM_TYPES, verbose_name='프로그램 유형')
    title = models.CharField(max_length=200, verbose_name='제목')
    description = models.TextField(verbose_name='설명')
    image1 = models.ImageField(upload_to='programs/', verbose_name='이미지 1', blank=True, null=True)
    image2 = models.ImageField(upload_to='programs/', verbose_name='이미지 2', blank=True, null=True)
    order = models.IntegerField(default=0, verbose_name='순서')
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    
    class Meta:
        ordering = ['program_type', 'order']
        verbose_name = '프로그램'
        verbose_name_plural = '프로그램'
    
    def __str__(self):
        return f"{self.get_program_type_display()} - {self.title}"


class Activity(models.Model):
    ACTIVITY_TYPES = (
        ('portfolio', '심슨 포트폴리오'),
        ('interview', '심슨 인터뷰'),
        ('contest', '심슨 콘테스트'),
    )
    
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES, verbose_name='활동 유형')
    title = models.CharField(max_length=200, verbose_name='제목')
    description = models.CharField(max_length=300, verbose_name='설명', blank=True)
    sub_description = models.CharField(max_length=300, verbose_name='부가 설명', blank=True)
    image = models.ImageField(upload_to='activities/', verbose_name='이미지', blank=True, null=True)
    order = models.IntegerField(default=0, verbose_name='순서')
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    
    class Meta:
        ordering = ['activity_type', 'order']
        verbose_name = '학원 활동'
        verbose_name_plural = '학원 활동'
    
    def __str__(self):
        return f"{self.get_activity_type_display()} - {self.title}"


class SpecialSchoolResult(models.Model):
    school = models.CharField(max_length=100, verbose_name='특목고')
    department = models.CharField(max_length=100, verbose_name='학과', blank=True)
    student_name = models.CharField(max_length=50, verbose_name='학생 이름')
    middle_school = models.CharField(max_length=100, verbose_name='중학교')
    year = models.IntegerField(verbose_name='합격년도')
    order = models.IntegerField(default=0, verbose_name='순서')
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    
    class Meta:
        ordering = ['-year', 'order']
        verbose_name = '특목고 합격자'
        verbose_name_plural = '특목고 합격자'
    
    def __str__(self):
        return f"{self.school} {self.department} - {self.student_name}"