from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from admission.models import StudentDetails
import datetime

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
    try:
        details = StudentDetails(student_first_name = student_first_name,
                                student_middle_name = student_middle_name,
                                student_last_name = student_last_name,
                                student_age = student_age,
                                student_blood_grp = student_blood_grp,
                                student_gender = student_gender,
                                student_admission_to = student_admission_to,
                                student_dob = student_dob)
        details.save()
        return JsonResponse({'status' : 'success'})
    except:
        return JsonResponse({'status' : 'failure'})

    
