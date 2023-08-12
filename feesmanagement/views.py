from django.shortcuts import render
from django.http import HttpResponse
from . import helper
import json

# Create your views here.
def home(request):
    return render(request, 'home.html')

def classroomSummary(request):
    if request.method == 'GET':
        selectedClass = request.GET.get('selectedClass')
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

def profilePage(request):
    pass

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


def login(request):
    print('test')
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            helper.validate_teacher(username, password)
            request.session['logged_in'] = True
            print(request)
            return render(request, 'home.html')
        except:
            custom_404(request, 'Error')

def logout(request):
    request.session.clear()
    return render(request, 'home.html')

def custom_404(request, exception):
    print('Inside custom 404')
    return render(request, '404.html', status=404)