import logging
from .models import *
from .constants import *
import datetime
from django.http import Http404

def get_student_by_roll(roll_number):
    pass

def _get_pending_months():
    return 0


def _get_students_metadata_dict(stduents):
    students_metadata_dicts = []
    for student in stduents:
        student_dict = {}
        student_dict['student_name'] = student.student_name
        student_dict['student_roll'] = student.student_roll
        student_dict['fees_amount'] = student.fees_amount
        student_dict['pending_months'] = _get_pending_months()
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

def get_this_month_fees_data():
    pass



def add_fee_to_datastore(
        name: str, roll: str, selectedClass: int, date: str,
        month: str, amount: int, subjects: str
    ):
    standard = MAP_CLASS_NAME_TO_INT[selectedClass]
    amount = int(amount)
    logging.info('Saving Fee record..')
    fees = FeesRecord(
        name=name, amount=amount, date=date, standard=standard,
        month=month, subjects=subjects)
    fees.save()
    # Add this fees to the profile of the individual student.

def _get_student_fees_details(fees_object):
    student = {}
    student['name'] = fees_object.name
    student['date'] = fees_object.date
    student['amount'] = fees_object.amount
    student['standard'] = fees_object.standard
    student['subjects'] = fees_object.subjects
    student['month'] = fees_object.month
    return student

def get_current_month_fees_objects():
    current_date_object = datetime.date.today()
    current_date = (
        str(current_date_object.year) + '-' +
        str(current_date_object.month) + '-' +
        str(current_date_object.day))

    month_beginning_date = (
        str(current_date_object.year) + '-' +
        str(current_date_object.month) + '-' +
        str(1) #first day
    )

    # The fees objects which are collected this month.
    fees_objects = FeesRecord.objects.filter(
        date__gte=month_beginning_date, date__lte=current_date)

    monthly_stats = {
        'class_eight': [],
        'class_nine': [],
        'class_ten': [],
        'class_eleven_science': [],
        'class_eleven_commerce': [],
        'class_twelve_science': [],
        'class_twelve_commerce': []
    }

    class_eight_collection = 0
    class_nine_collection = 0
    class_ten_collection = 0
    class_eleven_science_collection = 0
    class_twelve_science_collection = 0
    class_eleven_commerce_collection = 0
    class_twelve_commerce_collection = 0

    for fee_object in fees_objects:
        student_fee_dict = _get_student_fees_details(fee_object)
        standard = student_fee_dict['standard']

        if standard == MAP_CLASS_NAME_TO_INT[CLASS_EIGHT]:
            class_eight_collection += student_fee_dict['amount']
            monthly_stats['class_eight'].append(student_fee_dict)

        elif standard == MAP_CLASS_NAME_TO_INT[CLASS_NINE]:
            class_nine_collection += student_fee_dict['amount']
            monthly_stats['class_nine'].append(student_fee_dict)

        elif standard == MAP_CLASS_NAME_TO_INT[CLASS_TEN]:
            class_ten_collection += student_fee_dict['amount']
            monthly_stats['class_ten'].append(student_fee_dict)

        elif standard == MAP_CLASS_NAME_TO_INT[CLASS_ELEVEN_COMMERCE]:
            class_eleven_commerce_collection += student_fee_dict['amount']
            monthly_stats['class_eleven_commerce'].append(student_fee_dict)

        elif standard == MAP_CLASS_NAME_TO_INT[CLASS_ELEVEN_SCIENCE]:
            class_eleven_science_collection += student_fee_dict['amount']
            monthly_stats['class_eleven_science'].append(student_fee_dict)

        elif standard == MAP_CLASS_NAME_TO_INT[CLSSS_TWELVE_COMMERCE]:
            class_twelve_commerce_collection += student_fee_dict['amount']
            monthly_stats['class_twelve_commerce'].append(student_fee_dict)

        elif standard == MAP_CLASS_NAME_TO_INT[CLASS_TWELVE_SCIENCE]:

            class_twelve_science_collection += student_fee_dict['amount']
            monthly_stats['class_twelve_science'].append(student_fee_dict)

    return monthly_stats


def validate_teacher(username, password):
    try:
        teacher = Teacher.objects.get(username=username)
        if teacher.password != password:
            raise Exception
    except:
        raise Exception