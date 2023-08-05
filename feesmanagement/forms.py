from django import forms

selected_class=[
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11 commerce','11 commerece'),
    ('11 science','11 science'),
    ('12 commerce','12 commerce'),
    ('12 science','12 science'),
]

class student_form(forms.Form):
    Name= forms.CharField(max_length=20)
    Class= forms.CharField(label="Select the class",widget=forms.Select(choices=selected_class))