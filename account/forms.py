from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'date_of_birth', 'gender', 'phone_no', 'home_address', 'next_of_kin_name', 'next_of_kin_phone_no', 'next_of_kin_address', 'relationship', 'reg_no', 'course', 'department', 'faculty', 'level', 'receipt_no']

class HostelForm(ModelForm):
    class Meta:
        model = Hostel
        fields = '__all__'

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class WardenForm(ModelForm):
    class Meta:
        model = Warden
        fields = '__all__'


class ApplyForHostelForm(ModelForm):
    class Meta:
        model = Apply
        fields = ['favourite_hostel',]
