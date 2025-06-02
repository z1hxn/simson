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