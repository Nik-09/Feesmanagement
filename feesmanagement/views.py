import calendar
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from feesmanagement.models import StudentClassEight
from . import helper
from .forms import student_form
from django.db.models.functions import ExtractMonth
from . import const
import json
import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile_visit(request):
    form={}
    form['form']=student_form()
    return render(request, 'student-profile.html', form)

def classroomSummary(request):
    if request.method == 'GET':
        selectedClass = request.GET.get('selectedClass')
        print(selectedClass)
        students = helper.get_all_students_from_class(selectedClass)
        total_students = len(students)
        amount_due = 0
        number_of_students_with_clear_dues = 1
        number_of_students_with_unclear_dues = 4

        return render(
            request, 'classroom-summary.html', {
                'students': students,
                'totalStudents': total_students,
                'amountDue': amount_due,
                'numberOfStudentsWithClearDues': number_of_students_with_clear_dues,
                'numberOfStudentsWithUnclearDues': number_of_students_with_unclear_dues,
            }
        )
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
        student = helper.get_student_by_name(selectedClass, name)
        print('pritam')
        fees = {}
        student_dict ={}
        student_fees ={}
        sum=0
        student_fees= helper.get_monthly_status(
        student, selectedClass)
        # print(student.joining_date.month)
        # for key in student_fees:
        #     if student_fees[key] == None and key <= student.joining_date.month:
        #         sum = sum+1
        student_dict['student_name'] = student.student_name
        student_dict['student_class'] = student.student_class
        student_dict['student_roll'] = student.student_roll
        student_dict['joining_date']=student.joining_date
        student_dict['fees_amount']=student.fees_amount
        student_dict['school_name']=student.school_name
        student_dict['guardian_mobile_number']=student.guardian_mobile_number
        student_dict['student_mobile_number']=student.student_mobile_number
        fees_color={}
        list_of_dict = []
        integer = 0
        month = const.month
        current_month = datetime.datetime.now()
        current_date = datetime.datetime.now()
        print(month[8])
        if name != student.student_name:
            return render(request, 'home.html')
        for key in student_fees:
            variable = {}
            if student_dict['joining_date'].month > key:
                variable['grey'] = month[key]
            elif student_dict['joining_date'].month == key:
                if student.joining_date.strftime("%d") <= '20' and student_fees[key]==None:
                    variable['red'] = month[key]
                    sum=sum+1
                elif student_fees[key]!=None:
                    variable['green']= month[key]
                else:
                    variable['grey']=month[key]
            elif student_dict['joining_date'].month < key:
                if student_fees[key] != None:
                    variable['green'] = month[key]
                elif current_month.month >= key and student_fees[key] == None:
                    variable['red'] = month[key]
                    sum=sum+1
                else:
                    variable['grey']=month[key]
            list_of_dict.append(variable)
            students =list_of_dict
        student_dict['pending_months']=sum
        print(students)
        return render(request, 'profile.html', {'students':students, 'student_dict': student_dict})

def feesRecordFormPage(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        selectedClass = request.POST.get('selectedClass')
        date = request.POST.get('date')
        month = request.POST.get('selectedMonth')
        amount = request.POST.get('amount')

        # Collecting subjects
        # TODO: Add validator for subjects.
        subjects = request.POST.getlist('subjects')
        jsonified_subjects = json.dumps(subjects)
        print(subjects, jsonified_subjects)
        # if subjects is not None:
            # print(subjects, jsonified_subjects)

        helper.add_fee_to_datastore(
            name, roll, selectedClass, date, month, amount, jsonified_subjects)

    return render(request, 'fees-record-form.html')


def monthlyStatsPage(request):
    helper.get_current_month_fees_objects()
    return render(request, 'monthly-stats.html')




            # if student.student_name == name and(student.student_class==8 or ):
                # fees[1]=student.january_fees_date
                # fees[2]=student.february_fees_date
                # fees[3]=student.march_fees_date
                # fees[4]=student.april_fees_date
                # fees[5]=student.may_fees_date
                # fees[6]=student.june_fees_date
                # fees[7]=student.july_fees_date
                # fees[8]=student.august_fees_date
                # fees[9]=student.september_fees_date
                # fees[10]=student.october_fees_date
                # fees[11]=student.november_fees_date
                # fees[12]=student.december_fees_date
                # for key in fees:
                #     if fees[key] != None:
                #         sum = sum+1
                # student_dict['student_name'] = student.student_name
                # student_dict['student_class'] = student.student_class
                # student_dict['pending_months'] = sum
                # student_dict['student_roll'] = student.student_roll
                # student_dict['joining_date']=student.joining_date
                # student_dict['fees_amount']=student.fees_amount
                # student_dict['school_name']=student.school_name
                # student_dict['january_fees_date']=student.january_fees_date
                # student_dict['february_fees_date']=student.february_fees_date
                # student_dict['march_fees_date']=student.march_fees_date
                # student_dict['april_fees_date']=student.april_fees_date
                # student_dict['may_fees_date']=student.may_fees_date
                # student_dict['june_fees_date']=student.june_fees_date
                # student_dict['july_fees_date']=student.july_fees_date
                # student_dict['august_fees_date']=student.august_fees_date
                # student_dict['september_fees_date']=student.september_fees_date
                # student_dict['october_fees_date']=student.october_fees_date
                # student_dict['november_fees_date']=student.november_fees_date
                # student_dict['december_fees_date']=student.december_fees_date



                       # for key in student_fees:
        #     if student_dict['joining_date'].month > key:
        #         variable['color'+ str(integer)]='grey'
        #         variable['value'+ str(integer)]=month[key]
        #     elif student_dict['joining_date'].month < key and student_fees[key] != None:
        #         variable['color' + str(integer)]='Green'
        #         variable['value' + str(integer)]=month[key]
        #     integer=integer+1