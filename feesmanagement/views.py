from django.shortcuts import render
from django.http import HttpResponse
from . import helper
from .forms import student_form

# Create your views here.
def home(request):
    form={}
    form['form']=student_form()
    return render(request, 'home.html', form)

def classroomSummary(request):
    if request.method == 'GET':
        selectedClass = request.GET.get('selectedClass')
        students = helper.get_all_students_from_class(selectedClass)
        print(students, 'Nikhil')
        return render(request, 'classroom-summary.html', {'students':students})
    else:
        return render(request, 'classroom-summary.html')

def profilePage(request):
    pass

def login_auth(request):
    if request.method == 'POST':
        form = request.POST.get('Name')