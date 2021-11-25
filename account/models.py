from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#     is_warden = models.BooleanField(default=False)


class Student(models.Model):
    # user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    gender_choices = [
        ('Male', 'Male'), 
        ('Female', 'Female')
    ]
    reg_choices = [
        ('Pending', 'Pending'), 
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    level_choices = [
        ('100L', '100L'), 
        ('200L', '200L'),
        ('300L', '300L'),
        ('400L', '400L'),
        ('500L', '500L'),
    ]
    # student's personal informations
    first_name = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    date_of_birth = models.DateField(max_length=10, help_text="format: YYY-MM-DD", null=True)
    gender = models.CharField(choices=gender_choices, max_length=6, default=None, null=True)
    email = models.CharField(max_length=200, null=True)
    phone_no = models.CharField(max_length=11, null=True)
    home_address = models.CharField(max_length=200, null=True)
    next_of_kin_name = models.CharField(max_length=200, null=True)
    next_of_kin_phone_no = models.CharField(max_length=200, null=True)
    next_of_kin_address = models.CharField(max_length=200, null=True)
    relationship = models.CharField(max_length=200, null=True)
    # student's bio-data
    reg_no = models.CharField(max_length=200, null=True, unique=True)
    course = models.CharField(max_length=200, null=True)
    faculty = models.ForeignKey('faculty', null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey('department', null=True, on_delete=models.SET_NULL)
    level = models.CharField(choices=level_choices, max_length=4, null=True)
    hostel = models.ForeignKey('hostel', null=True, on_delete=models.SET_NULL)
    room_no = models.ForeignKey('room', null=True, on_delete=models.SET_NULL)
    bed_no = models.OneToOneField('bed', null=True, on_delete=models.SET_NULL)
    receipt_no = models.CharField(max_length=200, null=True, unique=True, help_text="Ensure you enter a valid receipt number.")
    reg_status = models.CharField(choices=reg_choices, max_length=10, default=None, null=True)
    date_of_created = models.DateTimeField(auto_now_add=True)
    room_allotted = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name)


class Course(models.Model):
    name = models.CharField(max_length=200, null=True)
    department = models.OneToOneField('department', null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200, null=True)
    faculty = models.ForeignKey('faculty', null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name


class Warden(models.Model):
    title_choice = [
        ('mr', 'Mr'),
        ('miss', 'Miss'),
        ('mrs', 'Mrs'),
    ]
    qualification_choice = [
        ('BSc', 'BSc'),
        ('HND', 'HND'),
        ('ND', 'ND'),
    ]
    title = models.CharField(choices=title_choice, max_length=4, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    qualification = models.CharField(choices=qualification_choice, max_length=3, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    hostel = models.OneToOneField('Hostel',null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Room(models.Model):
    room_choice = [
        ('classic', 'Classic'),
        ('premium', 'Premium'),
    ]

    room_no = models.CharField(max_length=10, null=True)

    room_type = models.CharField(choices=room_choice, max_length=7, default=None)
    vacant = models.BooleanField(default=False)
    # make a dropdown of all available hostels
    # users can only a unique room to any hostel
    hostel = models.ForeignKey('Hostel', null=True,on_delete=models.CASCADE,)
    facilities = models.CharField(max_length=100, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.room_no

class Bed(models.Model):
    bed_no = models.CharField(max_length=100, 
    null=True)
    hostel = models.ForeignKey('hostel', null=True, on_delete= models.CASCADE)
    # display rooms related to the selected hostel above
    room = models.CharField(max_length=200, null=True)
    
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.bed_no

class Hostel(models.Model):
    gender_choices = [
        ('Male', 'Male'), 
        ('Female', 'Female')
    ]

    name = models.CharField(max_length=200)
    gender = models.CharField(choices=gender_choices, max_length=6, default=None, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # warden = models.OneToOneField(Warden, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name


class Allocate(models.Model):
    status_choice = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices=status_choice, null=True, max_length=100)
    # student = models.ForeignKey('Student', null=True, on_delete=models.SET_NULL)
    # room = models.OneToOneField('Room', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.status


class Apply(models.Model):

    favourite_hostel = models.CharField(max_length=200, null=True)
    room_alloted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class Leave(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=100,blank = False)
    accept = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    confirm_time = models.DateTimeField(auto_now_add=True)
