from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = '심슨어학원 프로필'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)