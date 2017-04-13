import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from admission.models import StudentDetails, ClassDetails
from datetime import datetime
from common.data_validation import DataValidation
import re
import sys

from django.core import serializers

def save_data(request):
    student_first_name = request.POST.get('st_fn')
    student_middle_name = request.POST.get('st_mn')
    student_last_name = request.POST.get('st_ln')
    # student_age = request.POST.get('st_age')
    student_blood_grp = request.POST.get('st_bg')
    student_gender = request.POST.get('st_gen')
    student_admission_to = request.POST.get('st_a2')
    student_dob = request.POST.get('st_dob')

    standard = ['LKG','UKG','Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9',

                'Class10', 'Class11', 'Class12']
    gender = ['Male','Female','Other']

    data_val = DataValidation()
    student_first_name = data_val.__primary_data_validation__('name_space', student_first_name, 'Student First Name')
    if student_middle_name != "":
        student_middle_name = data_val.__primary_data_validation__('name_space', student_middle_name, 'Student Middle Name')
    student_last_name = data_val.__primary_data_validation__('name_space', student_last_name, 'Student Last Name')
    # student_age = data_val.__primary_data_validation__('^[0-9]*[0-9]$', student_age, 'Student Age')
    student_blood_grp = data_val.__primary_data_validation__('blood_grp', student_blood_grp, 'Student Blood Group')
    student_gender = data_val.__specific_data_validation__(gender, student_gender, 'Gender')
    student_admission_to = data_val.__specific_data_validation__(standard, student_admission_to, 'Admission to')
    student_dob = data_val.__primary_data_validation__('date', student_dob, 'Student DOB')
    if student_dob != "":
        student_age = data_val.__age_calculate__(student_dob)


    if student_admission_to != "":
        data_val.__class_validate__(student_admission_to)

    try:
        if len(data_val.invalid_param) > 0:
            invalid_string = ''
            for i in data_val.invalid_param:
                invalid_string += i+', '
            else:
                invalid_string += 'are invalid parameters'
            # DataValidation.invalid_param = []
            return JsonResponse({'status': 'Failed',
                                'message': invalid_string})
    except:
        return JsonResponse({'status': 'Failed',
                            'message': sys.exc_info()})


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
