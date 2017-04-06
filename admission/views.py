from django.shortcuts import render
from models import StudentDetails

# Create your views here.

def save_data(request):
    student_first_name = request.GET.get('first_name')
    student_middle_name = request.GET.get('middle_name')
    student_last_name = request.GET.get('last_name')
    student_age = request.GET.get('age')
    student_blood_grp = request.GET.get('blood_grp')
    student_gender = request.GET.get('gender')
    student_admission_to = request.GET.get('admission_to')
    student_dob = request.GET.get('DOB')

    details = StudentDetails(student_first_name = student_first_name,
                    student_middle_name =student_middle_name,
                    student_last_name = student_last_name,
                    student_age = student_age,
                    student_blood_grp = student_blood_grp,
                    student_gender = student_gender,
                    student_admission_to = student_admission_to,
                    student_dob = student_dob)
    details.save()
    return

