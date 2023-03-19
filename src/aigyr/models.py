from django.db import models


class Attendance(models.Model):
    date = models.DateField()


class Group(models.Model):
    name = models.CharField(max_length=30)


class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=11)
    balance = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL)
    attendance = models.ManyToManyField(Attendance)


class Teacher(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
