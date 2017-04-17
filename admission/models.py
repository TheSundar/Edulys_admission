from __future__ import unicode_literals

from django.db import models

# Create your models here.

class StudentDetails(models.Model):
    blood_grp = (('O+','O_Pos'),
                 ('O-','O_Neg'),
                 ('B+', 'B_Pos'),
                 ('B-', 'B_Neg'),
                 ('A+', 'A_Pos'),
                 ('A-', 'A_Neg'),
                 ('AB+', 'AB_Pos'),
                 ('AB-', 'AB_Neg'))
    gender = (('Male','Male'),
              ('Female','Female'),
              ('Other','Other'))
    student_first_name = models.CharField(max_length=40)
    student_middle_name = models.CharField(max_length=40)
    student_last_name = models.CharField(max_length=40)
    student_age = models.IntegerField(default=0)
    student_blood_grp = models.CharField(max_length=10)
    student_gender = models.CharField(max_length=10)
    student_admission_to = models.CharField(max_length=100)
    student_dob = models.DateField()

class ParentsDetails(models.Model):
    student = models.ForeignKey(StudentDetails, blank=True)
    parent_type = models.CharField(max_length=40)
    parent_first_name = models.CharField(max_length=40)
    parent_middle_name = models.CharField(max_length=40)
    parent_last_name = models.CharField(max_length=40)
    parent_occupation = models.CharField(max_length=50)
    parent_income_pa = models.IntegerField(max_length=20)
    parent_phone_number_1 = models.CharField(max_length=20)
    parent_phone_number_2 = models.CharField(max_length=20)


class ClassDetails(models.Model):
    class_name = models.CharField(max_length=100)


