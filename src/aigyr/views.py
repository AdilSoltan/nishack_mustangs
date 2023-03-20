from django.shortcuts import render
from rest_framework.response import Response
from .models import Student, Teacher
from rest_framework.views import APIView
from .serializer import StudentSerializer, TeacherSerializer

# def regIn(request):
#         if request.POST.get("role") == "Student":
#             student = Student()
#             student.first_name = request.POST.get("first_name")
#             student.last_name = request.POST.get("last_name")
#             student.email = request.POST.get("email")
#             student.password = request.POST.get("password")
#             student.phone_number = request.POST.get("phone_number")
#         if request.POST.get("role") == "Teacher":
#             teacher = Teacher()
#             teacher.first_name = request.POST.get("first_name")
#             teacher.last_name = request.POST.get("last_name")
#             teacher.email = request.POST.get("email")
#             teacher.password = request.POST.get("password")
#             teacher.phone_number = request.POST.get("phone_number")
#         return HttpResponseRedirect("/")


class RegIn(APIView):
    def get(self, request):
        if request.POST.get("role") == "Teacher":
            output = [
                {
                    "first_name": output.first_name,
                    "last_name": output.last_name,
                    "phone_number": output.phone_number,
                    "email": output.email,
                    "password": output.password,
                    "group": output.group
                } for output in Teacher.objects.all()
            ]
            return Response(output)
        if request.POST.get("role") == "Student":
            output = [
                {
                    "first_name": output.first_name,
                    "last_name": output.last_name,
                    "phone_number": output.phone_number,
                    "email": output.email,
                    "password": output.password,
                    "group": output.group,
                    "balance": output.balance,
                    "attendance": output.attendance
                } for output in Student.objects.all()
            ]
            return Response(output)

    # def post(self, request):
    #     serial

