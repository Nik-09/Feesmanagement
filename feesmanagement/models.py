from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class BaseStudentModel(models.Model):
    # Student's personal data
    student_name = models.CharField(max_length=64)
    student_class = models.IntegerField(
        default=8, null=False, validators=[MinValueValidator(8), MaxValueValidator(12)])
    student_mobile_number = models.CharField(max_length=10, null=True)
    student_roll = models.CharField(max_length=6, null=True)
    joining_date = models.DateField(default=timezone.now)
    fees_amount = models.IntegerField(default=0, null=False)
    school_name = models.CharField(max_length=64, null=True)
    guardian_mobile_number = models.CharField(max_length=10, null=True)
    subjects = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.student_name + " " + str(self.id)



# Child model classes derived from BaseStudentModel

class StudentClassEight(BaseStudentModel):

    class Meta:
        verbose_name = 'Class Eight'
        verbose_name_plural = 'Class Eight Records'

    # Date for each month
    january_fees_date = models.DateField(null=True, blank=True)
    february_fees_date = models.DateField(null=True, blank=True)
    march_fees_date = models.DateField(null=True, blank=True)
    april_fees_date = models.DateField(null=True, blank=True)
    may_fees_date = models.DateField(null=True, blank=True)
    june_fees_date = models.DateField(null=True, blank=True)
    july_fees_date = models.DateField(null=True, blank=True)
    august_fees_date = models.DateField(null=True, blank=True)
    september_fees_date = models.DateField(null=True, blank=True)
    october_fees_date = models.DateField(null=True, blank=True)
    november_fees_date = models.DateField(null=True, blank=True)
    december_fees_date = models.DateField(null=True, blank=True)

class StudentClassNine(BaseStudentModel):
    class Meta:
        verbose_name = 'Class Nine'
        verbose_name_plural = 'Class Nine Records'

    # Date for each month
    january_fees_date = models.DateField(null=True, blank=True)
    february_fees_date = models.DateField(null=True, blank=True)
    march_fees_date = models.DateField(null=True, blank=True)
    april_fees_date = models.DateField(null=True, blank=True)
    may_fees_date = models.DateField(null=True, blank=True)
    june_fees_date = models.DateField(null=True, blank=True)
    july_fees_date = models.DateField(null=True, blank=True)
    august_fees_date = models.DateField(null=True, blank=True)
    september_fees_date = models.DateField(null=True, blank=True)
    october_fees_date = models.DateField(null=True, blank=True)
    november_fees_date = models.DateField(null=True, blank=True)
    december_fees_date = models.DateField(null=True, blank=True)

class StudentClassTen(BaseStudentModel):
    class Meta:
        verbose_name = 'Class Ten'
        verbose_name_plural = 'Class Ten Records'

    # Date for each month
    december_fees_date = models.DateField(null=True, blank=True)
    january_fees_date = models.DateField(null=True, blank=True)
    february_fees_date = models.DateField(null=True, blank=True)
    march_fees_date = models.DateField(null=True, blank=True)
    april_fees_date = models.DateField(null=True, blank=True)
    may_fees_date = models.DateField(null=True, blank=True)
    june_fees_date = models.DateField(null=True, blank=True)
    july_fees_date = models.DateField(null=True, blank=True)
    august_fees_date = models.DateField(null=True, blank=True)
    september_fees_date = models.DateField(null=True, blank=True)
    october_fees_date = models.DateField(null=True, blank=True)
    november_fees_date = models.DateField(null=True, blank=True)
    january_fees_date = models.DateField(null=True, blank=True)
    february_fees_date = models.DateField(null=True, blank=True)

class StudentClassElevenCommerce(BaseStudentModel):
    class Meta:
        verbose_name = 'Class Eleven Commerce'
        verbose_name_plural = 'Class Eleven Commerce Records'

    # Date for each month
    april_fees_date = models.DateField(null=True, blank=True)
    may_fees_date = models.DateField(null=True, blank=True)
    june_fees_date = models.DateField(null=True, blank=True)
    july_fees_date = models.DateField(null=True, blank=True)
    august_fees_date = models.DateField(null=True, blank=True)
    september_fees_date = models.DateField(null=True, blank=True)
    october_fees_date = models.DateField(null=True, blank=True)
    november_fees_date = models.DateField(null=True, blank=True)
    january_fees_date = models.DateField(null=True, blank=True)
    february_fees_date = models.DateField(null=True, blank=True)

class StudenClassElevenScience(BaseStudentModel):
    class Meta:
        verbose_name = 'Class Eleven Science'
        verbose_name_plural = 'Class Eleven Science Records'

    # Date for each month
    april_fees_date = models.DateField(null=True, blank=True)
    may_fees_date = models.DateField(null=True, blank=True)
    june_fees_date = models.DateField(null=True, blank=True)
    july_fees_date = models.DateField(null=True, blank=True)
    august_fees_date = models.DateField(null=True, blank=True)
    september_fees_date = models.DateField(null=True, blank=True)
    october_fees_date = models.DateField(null=True, blank=True)
    november_fees_date = models.DateField(null=True, blank=True)
    january_fees_date = models.DateField(null=True, blank=True)
    february_fees_date = models.DateField(null=True, blank=True)

class StudentClassTwelveCommerce(BaseStudentModel):
    class Meta:
        verbose_name = 'Class Twelve Commerce'
        verbose_name_plural = 'Class Twelve Commerce Records'

    # Date for each month
    april_fees_date = models.DateField(null=True, blank=True)
    may_fees_date = models.DateField(null=True, blank=True)
    june_fees_date = models.DateField(null=True, blank=True)
    july_fees_date = models.DateField(null=True, blank=True)
    august_fees_date = models.DateField(null=True, blank=True)
    september_fees_date = models.DateField(null=True, blank=True)
    october_fees_date = models.DateField(null=True, blank=True)
    november_fees_date = models.DateField(null=True, blank=True)
    january_fees_date = models.DateField(null=True, blank=True)
    february_fees_date = models.DateField(null=True, blank=True)

class StudentClassTwelveScience(BaseStudentModel):
    class Meta:
        verbose_name = 'Class Twelve Science'
        verbose_name_plural = 'Class Twelve Science Records'

    # Date for each month
    april_fees_date = models.DateField(null=True, blank=True)
    may_fees_date = models.DateField(null=True, blank=True)
    june_fees_date = models.DateField(null=True, blank=True)
    july_fees_date = models.DateField(null=True, blank=True)
    august_fees_date = models.DateField(null=True, blank=True)
    september_fees_date = models.DateField(null=True, blank=True)
    october_fees_date = models.DateField(null=True, blank=True)
    november_fees_date = models.DateField(null=True, blank=True)
    january_fees_date = models.DateField(null=True, blank=True)
    february_fees_date = models.DateField(null=True, blank=True)
