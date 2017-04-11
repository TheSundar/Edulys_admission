import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from admission.models import StudentDetails, ClassDetails
import datetime

import re
import sys

from django.core import serializers



# Create your views here.

class DataValidation(object):
    invalid_param = []

    def __init__(self):
        pass

    def __primary_data_validation__(self,pattern, value, param):
        self.__pattern = pattern
        self.__value = value
        self.__param = param
        if self.__value != None and self.__value != '':
            if re.findall(self.__pattern, self.__value) != []:
                return self.__value
            else:
                DataValidation.invalid_params.append(self.__param)
                return ""
        else:
            DataValidation.invalid_params.append(self.__param)
            return ""

    def __specific_data_validation__(self, data_list, value, param):
        self.__data_list = data_list
        self.__value = value
        self.__param = param
        if self.__value in self.__data_list:
            return self.__value
        else:
            DataValidation.invalid_param.append(self.__param)
            return ""

    def __age_calculate__(self,DOB):
        self.__DOB = DOB
        b_date = datetime.strptime(self.__DOB, '%Y-%m-%d')
        return (datetime.today() - b_date).days/365

    def __class_validate__(self,admit_to):
        self.__admit_to = admit_to
        if admit_to == 'LKG':
            self.__class_enum = -1
        elif admit_to == 'UKG':
            self.__class_enum = 0
        else:
            self.__class_enum = re.findall('Class([\d]+)',admit_to)[0]

        if 5-()

def save_data(request):
    student_first_name = request.GET.get('st_fn')
    student_middle_name = request.GET.get('st_mn')
    student_last_name = request.GET.get('st_ln')
    # student_age = request.GET.get('st_age')
    student_blood_grp = request.GET.get('st_bg')
    student_gender = request.GET.get('st_gen')
    student_admission_to = request.GET.get('st_a2')
    student_dob = request.GET.get('st_dob')

    standard = ['LKG','UKG','Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9',

                'Class10', 'Class11', 'Class12']
    gender = ['Male','Female','Other']

    data_val = DataValidation()
    student_first_name = data_val.__primary_data_validation__('^[a-zA-Z]*[a-zA-Z]$', student_first_name, 'Student Middle Name')
    student_middle_name = data_val.__primary_data_validation__('^[a-zA-Z]*[a-zA-Z]$', student_middle_name, 'Student Middle Name')
    student_last_name = data_val.__primary_data_validation__('^[a-zA-Z]*[a-zA-Z]$', student_last_name, 'Student Last Name')
    # student_age = data_val.__primary_data_validation__('^[0-9]*[0-9]$', student_age, 'Student Age')
    student_blood_grp = data_val.__primary_data_validation__('^[a-bA-BoO]+[+-]$', student_blood_grp, 'Student Blood Group')
    student_gender = data_val.__specific_data_validation__(gender, student_gender, 'Gender')
    student_admission_to = data_val.__specific_data_validation__(standard, student_admission_to, 'Admission to')
    student_dob = data_val.__primary_data_validation__('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', student_dob, 'Student DOB')
    if student_dob != "":
        student_age = data_val.__age_calculate__(student_dob)


    if student_admission_to != "":


    try:
        if len(DataValidation.invalid_param) > 0:
            invalid_string = ''
            for i in DataValidation.invalid_param:
                invalid_string += i+' '
            else:
                invalid_string += 'are invalid parameters'
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
