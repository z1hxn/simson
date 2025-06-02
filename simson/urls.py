from django.contrib import admin
from django.urls import path, include
from main import views  # main 앱의 views.py에서 함수들을 불러옴

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # simson 앱의 URL을 포함
    path('student/', include('student.urls')),  # student 앱의 URL을 포함
    path('teacher/', include('teacher.urls')),  # teacher 앱의 URL을 포함
]