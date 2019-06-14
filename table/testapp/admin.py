from django.contrib import admin
from testapp.models import employee

class employeeadmin(admin.ModelAdmin):
    list_display = ['eno','esal','ename','ecity']

admin.site.register(employee,employeeadmin)
