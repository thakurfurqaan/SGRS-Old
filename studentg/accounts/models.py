from django.db import models
from django.contrib.auth.models import User
from redressal.models import University, Institute, Department, Redressal_Body
# Create your models here.


class Sys_User(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, parent_link=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    STUDENT = 'ST'
    UNIVERSITY = 'UNI'
    INSTITUTE = 'INS'
    DEPARTMENT = 'DEP'
    UNI_HEAD = 'UNI_H'
    INS_HEAD = 'INS_H'
    DEP_HEAD = 'DEP_H'
    DESIGNATION_CHOICES = [
        (STUDENT, 'Student'),
        (UNIVERSITY, 'University'),
        (INSTITUTE, 'Institute'),
        (DEPARTMENT, 'Department'),
        (UNI_HEAD, 'University_H'),
        (INS_HEAD, 'INSTITUTE_H'),
        (DEP_HEAD, 'Department_H'),
    ]
    designation = models.CharField(max_length=15, choices=DESIGNATION_CHOICES)


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    rollno=models.IntegerField(unique=True)

class University_Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

class Institute_Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

class Department_Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

'''
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
self.uid = urlsafe_base64_encode(force_bytes(user.pk))
self.token = default_token_generator.make_token(user)
'''
class Temp_User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.EmailField()
    redressal_body = models.ForeignKey(Redressal_Body, on_delete=models.CASCADE)
    STUDENT = 'ST'
    UNIVERSITY = 'UNI'
    INSTITUTE = 'INS'
    DEPARTMENT = 'DEP'
    UNI_HEAD = 'UNI_H'
    INS_HEAD = 'INS_H'
    DEP_HEAD = 'DEP_H'
    DESIGNATION_CHOICES = [
        (STUDENT, 'Student'),
        (UNIVERSITY, 'University'),
        (INSTITUTE, 'Institute'),
        (DEPARTMENT, 'Department'),
        (UNI_HEAD, 'University_H'),
        (INS_HEAD, 'INSTITUTE_H'),
        (DEP_HEAD, 'Department_H'),
    ]
    designation = models.CharField(max_length=15, choices=DESIGNATION_CHOICES)
    uidb64=models.CharField(max_length=255)
    token=models.CharField(max_length=255)