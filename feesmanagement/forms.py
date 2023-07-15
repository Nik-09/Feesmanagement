from django import forms


class student_form(forms.Form):
    Name= forms.CharField(max_length=20)