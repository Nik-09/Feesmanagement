import logging
from .models import *
from .constants import *
import datetime

def get_student_by_name(class_standard):
    if class_standard == '8':
        students = StudentClassEight.objects.all()
    elif class_standard == '9':
        students = StudentClassNine.objects.all()
    elif class_standard == '10':
        students = StudentClassTen.objects.all()
    elif class_standard == '11 commerce':
        students = StudentClassElevenCommerce.objects.all()
    elif class_standard == '11 science':
        students = StudenClassElevenScience.objects.all()
    elif class_standard == '12 commerce':
        students = StudentClassTwelveCommerce.objects.all()
    elif class_standard == '12 science':
        students = StudentClassTwelveScience.objects.all()
    else:
        raise Exception('Class not found')

    return students


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

    # hs prefix below means higher secondary
    hs_chemistry_collection = 0
    hs_physics_collection = 0
    hs_maths_collection = 0
    hs_biology_collection = 0
    hs_economics_collection = 0
    hs_business_studies_collection = 0
    hs_accounts_collection = 0
    # s prefix below means secondary
    s_all_subjects = 0
    s_only_science_subjects = 0

    subject_wise_collection = {
        'hs_chemistry_collection': hs_chemistry_collection,
        'hs_physics_collection': hs_physics_collection,
        'hs_maths_collection': hs_maths_collection,
        'hs_biology_collection': hs_biology_collection,
        'hs_economics_collection': hs_economics_collection,
        'hs_business_studies_collection': hs_business_studies_collection,
        'hs_accounts_collection': hs_accounts_collection,
        's_all_subjects': s_all_subjects,
        's_only_science_subjects': s_only_science_subjects
    }