from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, MainSlider, Philosophy, Achievement, UniversityResult, Program, Activity, SpecialSchoolResult


admin.site.site_header = "Simson Developer Admin Page"
admin.site.site_title = "Simson Admin"
admin.site.index_title = "심슨어학원 관리자 페이지"

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = '심슨어학원 프로필'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# 메인 페이지 콘텐츠 관리 Admin 클래스들
@admin.register(MainSlider)
class MainSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'subtitle')
    ordering = ('order',)
    
    fieldsets = (
        ('기본 정보', {
            'fields': ('title', 'subtitle', 'image')
        }),
        ('설정', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(Philosophy)
class PhilosophyAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    ordering = ('order',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'is_highlight', 'order', 'is_active')
    list_editable = ('order', 'is_highlight', 'is_active')
    list_filter = ('year', 'is_highlight', 'is_active')
    search_fields = ('title', 'description')
    ordering = ('-year', 'order')


@admin.register(UniversityResult)
class UniversityResultAdmin(admin.ModelAdmin):
    list_display = ('university', 'department', 'student_name', 'high_school', 'branch', 'year', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('year', 'university', 'branch', 'is_active')
    search_fields = ('university', 'department', 'student_name', 'high_school')
    ordering = ('-year', 'order')
    
    fieldsets = (
        ('학생 정보', {
            'fields': ('student_name', 'high_school', 'branch')
        }),
        ('합격 정보', {
            'fields': ('university', 'department', 'year')
        }),
        ('설정', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_type', 'title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('program_type', 'is_active')
    search_fields = ('title', 'description')
    ordering = ('program_type', 'order')
    
    fieldsets = (
        ('기본 정보', {
            'fields': ('program_type', 'title', 'description')
        }),
        ('이미지', {
            'fields': ('image1', 'image2'),
            'classes': ('collapse',)
        }),
        ('설정', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_type', 'title', 'description', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('activity_type', 'is_active')
    search_fields = ('title', 'description', 'sub_description')
    ordering = ('activity_type', 'order')
    
    fieldsets = (
        ('기본 정보', {
            'fields': ('activity_type', 'title', 'description', 'sub_description')
        }),
        ('이미지', {
            'fields': ('image',),
            'classes': ('collapse',)
        }),
        ('설정', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(SpecialSchoolResult)
class SpecialSchoolResultAdmin(admin.ModelAdmin):
    list_display = ('school', 'department', 'student_name', 'middle_school', 'year', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('year', 'school', 'is_active')
    search_fields = ('school', 'department', 'student_name', 'middle_school')
    ordering = ('-year', 'order')
    
    fieldsets = (
        ('학생 정보', {
            'fields': ('student_name', 'middle_school')
        }),
        ('합격 정보', {
            'fields': ('school', 'department', 'year')
        }),
        ('설정', {
            'fields': ('order', 'is_active')
        }),
    )


# Admin 사이트 메뉴 커스터마이징
class ContentManagementAdminSite(admin.AdminSite):
    site_header = "심슨어학원 콘텐츠 관리"
    site_title = "콘텐츠 관리"
    index_title = "콘텐츠 관리 대시보드"