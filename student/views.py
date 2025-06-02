from django.shortcuts import render

# Create your views here.

def student_view(request):
    return render(request, 'student.html')  # student.html 템플릿을 렌더링하여 반환_