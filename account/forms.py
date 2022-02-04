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
        fields = '__all__'
        exclude=['user']

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
        fields = '__all__'