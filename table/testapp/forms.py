from django import forms
from testapp.models import employee

class employeeform(forms.Modelforms):
    class Meta:
        model = employee
        fields  = "__all__"
