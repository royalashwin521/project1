import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'table.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake=Faker()


def populate(n):
    for i in range(n):
        fname = fake.name()
        fcity = fake.city()
        fno = randint(1000,5000)
        fsal = randint(10000,60000)
        employee.objects.get_or_create(ename = fname,ecity=fcity,eno = fno,esal=fsal)

populate(25)
