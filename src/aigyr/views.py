from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Student, Teacher

def regIn(request):
        if request.POST.get("role") == "Student":
            student = Student()
            student.first_name = request.POST.get("first_name")
            student.last_name = request.POST.get("last_name")
            student.email = request.POST.get("email")
            student.password = request.POST.get("password")
            student.phone_number = request.POST.get("phone_number")
        if request.POST.get("role") == "Teacher":
            teacher = Teacher()
            teacher.first_name = request.POST.get("first_name")
            teacher.last_name = request.POST.get("last_name")
            teacher.email = request.POST.get("email")
            teacher.password = request.POST.get("password")
            teacher.phone_number = request.POST.get("phone_number")
        return HttpResponseRedirect("/")