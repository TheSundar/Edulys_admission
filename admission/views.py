import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from admission.models import StudentDetails, ClassDetails
import datetime
import re

from django.core import serializers



# Create your views here.
def save_data(request):
    student_first_name = request.GET.get('st_fn')
    student_middle_name = request.GET.get('st_mn')
    student_last_name = request.GET.get('st_ln')
    student_age = request.GET.get('st_age')
    student_blood_grp = request.GET.get('st_bg')
    student_gender = request.GET.get('st_gen')
    student_admission_to = request.GET.get('st_a2')
    student_dob = request.GET.get('st_dob')
    Standard = ['LKG', 'UKG', 'Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9',
                'Class10', 'Class11', 'Class12']

    student_first_name = 'Invalid' if re.findall('^[a-zA-Z]*[a-zA-Z]$',
                                                 student_first_name) == [] else student_first_name
    student_middle_name = 'Invalid' if re.findall('^[a-zA-Z]*[a-zA-Z]$',
                                                  student_middle_name) == [] else student_middle_name
    student_last_name = 'Invalid' if re.findall('^[a-zA-Z]*[a-zA-Z]$', student_last_name) == [] else student_last_name
    student_age = 'Invalid' if re.findall('^[0-9]*[0-9]$', student_age) == [] else student_age
    student_blood_grp = 'Invalid' if re.findall('^[a-bA-B]+[+-]$', student_blood_grp) == [] else student_blood_grp
    student_gender = 'Invalid' if student_gender not in ['Male', 'Female', 'Other'] else student_gender
    student_admission_to = 'Invalid' if student_admission_to not in Standard else student_admission_to
    student_dob = 'Invalid' if re.findall('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', student_dob) == [] else student_dob

    if not (student_first_name != 'Invalid' and student_last_name != 'Invalid' and \
                        student_age != 'Invalid' and student_blood_grp != 'Invalid' and student_gender != 'Invalid' and \
                        student_admission_to != 'Invalid' and student_dob != 'Invalid'):
        return JsonResponse({'status': 'Failed',
                             'student_first_name': student_first_name,
                             'student_last_name': student_last_name,
                             'student_age': student_age,
                             'student_blood_grp': student_blood_grp,
                             'student_gender': student_gender,
                             'student_admission_to': student_admission_to,
                             'student_dob': student_dob})

    else:
        try:
            details = StudentDetails(student_first_name=student_first_name,
                                     student_middle_name=student_middle_name,
                                     student_last_name=student_last_name,
                                     student_age=student_age,
                                     student_blood_grp=student_blood_grp,
                                     student_gender=student_gender,
                                     student_admission_to=student_admission_to,
                                     student_dob=student_dob)

            details.save()
            return JsonResponse({'status': 'success', 'Message': 'Successfully saved to DB'})
        except:
            return JsonResponse({'status': 'failure', 'Message': 'Failed to saved to DB'})


def get_class(request):
    data = []
    class_data = ClassDetails.objects.all()
    for i in class_data:
        data.append({
            'id':i.id,
            'class_name':i.class_name
        })
    return JsonResponse({'status': 'success', 'data': data})
