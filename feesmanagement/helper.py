from .models import *
from .constants import *

def get_student_by_roll(roll_number):
    pass

def _get_students_metadata_dict(stduents):
    students_metadata_dicts = []
    for student in stduents:
        student_dict = {}
        student_dict['student_name'] = student.student_name
        student_dict['student_class'] = student.student_class
        student_dict['pending_months'] = 3
        student_dict['student_roll'] = student.student_roll
        students_metadata_dicts.append(student_dict)
    return students_metadata_dicts

def get_all_students_from_class(class_standard):
    if class_standard == CLASS_EIGHT:
        students = StudentClassEight.objects.all()
    elif class_standard == CLASS_NINE:
        students = StudentClassNine.objects.all()
    elif class_standard == CLASS_TEN:
        students = StudentClassTen.objects.all()
    elif class_standard == CLASS_ELEVEN_COMMERCE:
        students = StudentClassElevenCommerce.objects.all()
    elif class_standard == CLASS_ELEVEN_SCIENCE:
        students = StudenClassElevenScience.objects.all()
    elif class_standard == CLSSS_TWELVE_COMMERCE:
        students = StudentClassTwelveCommerce.objects.all()
    elif class_standard == CLASS_TWELVE_SCIENCE:
        students = StudentClassTwelveScience.objects.all()
    else:
        raise Exception('Class not found')

    return _get_students_metadata_dict(students)

