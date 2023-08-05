import calendar
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from feesmanagement.models import StudentClassEight
from . import helper
from .forms import student_form
from django.db.models.functions import ExtractMonth
from . import const

# Create your views here.
def home(request):
    form={}
    form['form']=student_form()
    return render(request, 'home.html', form)

def classroomSummary(request):
    if request.method == 'GET':
        selectedClass = request.GET.get('selectedClass')
        print(selectedClass)
        students = helper.get_all_students_from_class(selectedClass)
        print(students, 'Nikhil')
        return render(request, 'classroom-summary.html', {'students':students})
    else:
        return render(request, 'classroom-summary.html')

# def profilePage(request):
#     name = 'nikhil'
#     students = StudentClassEight.objects.all()
#     student_dict = {}
#     for student in students:
#         if student.student_name == name:
#             student_dict['student_name'] = student.student_name
#             student_dict['student_class'] = student.student_class
#             student_dict['pending_months'] = 3
#             student_dict['student_roll'] = student.student_roll
#             return render(request, 'profile.html', {'student_dict':student_dict})

def profilePage(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        selectedClass = request.POST.get('Class')
        students = helper.get_student_by_name(selectedClass)
        flag =1
        for student in students:
            student_dict = {}
            fees = {}
            if student.student_name == name:
                student_dict['student_name'] = student.student_name
                student_dict['student_class'] = student.student_class
                student_dict['pending_months'] = 3
                student_dict['student_roll'] = student.student_roll
                student_dict['joining_date']=student.joining_date
                student_dict['fees_amount']=student.fees_amount
                student_dict['school_name']=student.school_name
                student_dict['january_fees_date']=student.january_fees_date
                student_dict['february_fees_date']=student.february_fees_date
                student_dict['march_fees_date']=student.march_fees_date
                student_dict['april_fees_date']=student.april_fees_date
                student_dict['may_fees_date']=student.may_fees_date
                student_dict['june_fees_date']=student.june_fees_date
                student_dict['july_fees_date']=student.july_fees_date
                student_dict['august_fees_date']=student.august_fees_date
                student_dict['september_fees_date']=student.september_fees_date
                student_dict['october_fees_date']=student.october_fees_date
                student_dict['november_fees_date']=student.november_fees_date
                student_dict['december_fees_date']=student.december_fees_date
                fees[1]=student.january_fees_date
                fees[2]=student.february_fees_date
                fees[3]=student.march_fees_date
                fees[4]=student.april_fees_date
                fees[5]=student.may_fees_date
                fees[6]=student.june_fees_date
                fees[7]=student.july_fees_date
                fees[8]=student.august_fees_date
                fees[9]=student.september_fees_date
                fees[10]=student.october_fees_date
                fees[11]=student.november_fees_date
                fees[12]=student.december_fees_date

                print(fees[4])
                month = const.month
                return render(request, 'profile.html', {'student_dict':student_dict, 'month':month, 'fees': fees})
            else:
                flag=0
        if flag==0:
            return HttpResponse("The username is not valid")
