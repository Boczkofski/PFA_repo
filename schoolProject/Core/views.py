from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Core/index.html')
def add_student(request):
    return render(request, 'Core/add_student.html')