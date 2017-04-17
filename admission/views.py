import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from admission.models import StudentDetails, ClassDetails, ParentsDetails
from datetime import datetime
from common.data_validation import DataValidation
import re
import sys
from copy import deepcopy
import urllib2

from django.core import serializers

def save_data(request):
    data_val = DataValidation()
    check_student_data(request, data_val=data_val)
    check_parents_data(request, data_val=data_val)


def check_parents_data(request, data_val):
    # data_val = DataValidation()
    parent_details_list = []
    parent_details = urllib2.parse_http_list((request.POST.get('par_det')))
    print "PARENT : ",parent_details
    for i in parent_details:
        par_detail_dict = {}
        parent_type = i['type']
        parent_first_name = data_val.primary_data_validation('name_space', i['par_fn'], parent_type+' first_name')
        if i['par_mn'] != "":
            parent_middle_name = data_val.primary_data_validation('name_space', i['par_mn'], parent_type+' first_name')
        parent_last_name = data_val.primary_data_validation('name_space', i['par_ln'], parent_type+' first_name')
        parent_occupation = data_val.primary_data_validation('occupation', i['par_occ'], parent_type+' occupation')
        parent_income = data_val.primary_data_validation('income', i['par_inc'], parent_type+' income')
        parent_phone_num1 = data_val.primary_data_validation('phone_num', i['par_num1'], parent_type+' phone number 1')
        if i['par_num2'] != "":
            parent_phone_num2 = data_val.primary_data_validation('phone_num', i['par_num2'], parent_type + ' phone number 2')
        par_detail_dict['type'] = parent_type
        par_detail_dict['par_fn'] = parent_first_name
        par_detail_dict['par_mn'] = parent_middle_name
        par_detail_dict['par_ln'] = parent_last_name
        par_detail_dict['par_occ'] = parent_occupation
        par_detail_dict['par_inc'] = parent_income
        par_detail_dict['par_num1'] = parent_phone_num1
        par_detail_dict['par_num2'] = parent_phone_num2
        par_detail_dict_copy = deepcopy(par_detail_dict)
        parent_details_list.append(par_detail_dict_copy)
        par_detail_dict = {}
        if len(data_val.invalid_param) > 0:
            invalid_param_check(data_val=data_val)
        else:
            try:
                for i in parent_details_list:
                    par_details = ParentsDetails(parent_type=i['type'],
                                                 parent_first_name=i['par_fn'],
                                                 parent_middle_name=i['par_mn'],
                                                 parent_last_name=i['par_ln'],
                                                 parent_occupation=i['par_occ'],
                                                 parent_income_pa=i['par_inc'],
                                                 parent_phone_number_1=i['par_num1'],
                                                 parent_phone_number_2=i['par_num2'])
                    par_details.save()
            except:
                return JsonResponse({'status': 'failure', 'Message': 'Failed to save parents detals to db to DB'})

def check_student_data(request, data_val):
    student_first_name = request.POST.get('st_fn')
    student_middle_name = request.POST.get('st_mn')
    student_last_name = request.POST.get('st_ln')
    # student_age = request.POST.get('st_age')
    student_blood_grp = request.POST.get('st_bg')
    student_gender = request.POST.get('st_gen')
    student_admission_to = request.POST.get('st_a2')
    student_dob = request.POST.get('st_dob')
    parent_details = request.POST.get('par_det')

    standard = ['LKG','UKG','Class1', 'Class2', 'Class3', 'Class4', 'Class5', 'Class6', 'Class7', 'Class8', 'Class9',

                'Class10', 'Class11', 'Class12']
    gender = ['Male','Female','Other']

    # data_val = DataValidation()

    student_first_name = data_val.primary_data_validation('name_space', student_first_name, 'Student First Name')
    if student_middle_name != "":
        student_middle_name = data_val.primary_data_validation('name_space', student_middle_name, 'Student Middle Name')
    student_last_name = data_val.primary_data_validation('name_space', student_last_name, 'Student Last Name')
    # student_age = data_val.primary_data_validation('^[0-9]*[0-9]$', student_age, 'Student Age')
    student_blood_grp = data_val.primary_data_validation('blood_grp', student_blood_grp, 'Student Blood Group')
    student_gender = data_val.specific_data_validation(gender, student_gender, 'Gender')
    student_admission_to = data_val.specific_data_validation(standard, student_admission_to, 'Admission to')
    student_dob = data_val.primary_data_validation('date', student_dob, 'Student DOB')



    if student_dob != "":
        student_age = data_val.age_calculate(student_dob)


    if student_admission_to != "":
        data_val.class_validate(student_admission_to)

    if len(data_val.invalid_param) > 0:
        invalid_param_check(data_val=data_val)
    else:
        try:
            stu_details = StudentDetails(student_first_name=student_first_name,
                                     student_middle_name=student_middle_name,
                                     student_last_name=student_last_name,
                                     student_age=student_age,
                                     student_blood_grp=student_blood_grp,
                                     student_gender=student_gender,
                                     student_admission_to=student_admission_to,
                                     student_dob=student_dob)
            stu_details.save()
        except:
            return JsonResponse({'status': 'failure', 'Message': 'Failed to saved to DB'})


def invalid_param_check(data_val):
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



def get_class(request):
    data = []
    class_data = ClassDetails.objects.all()
    for i in class_data:
        data.append({
            'id':i.id,
            'class_name':i.class_name
        })
    return JsonResponse({'status': 'success', 'data': data})
