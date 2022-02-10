from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.

# class User(AbstractUser):
#     is_warden = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

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
    matric_no = models.CharField(max_length=200, null=True, unique=True)
    course = models.ForeignKey(
        'Course',
        null=True,
        default=None,
        on_delete=models.CASCADE)
    

    # faculty = models.OneToOneField('faculty', null=True, on_delete=models.CASCADE)
    # department = models.OneToOneField('department', null=True, on_delete=models.SET_NULL)

    level = models.CharField(choices=level_choices, max_length=4, null=True)

    receipt_no = models.CharField(max_length=200, null=True, unique=True, help_text="Ensure you enter a valid receipt number.")
    profile_pic = models.ImageField(default="default.jpg",null=True, blank=True)
    # reg_status = models.CharField(choices=reg_choices, max_length=10, default=None, null=True)
    date_of_created = models.DateTimeField(auto_now_add=True)
    hostel = models.ForeignKey(
        'Hostel',
        blank=True,
        on_delete=models.CASCADE,
        null=True)
    room = models.OneToOneField(
        'Room',
        blank=True,
        on_delete=models.CASCADE,
        null=True)
    room_allotted = models.BooleanField(default=False)
    no_dues = models.BooleanField(default=True)


    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name)


class Room(models.Model):
    room_choice = [('S', 'Single Occupancy'), ('D', 'Double Occupancy'), ('P', 'Reserved for Research Scholars'),('B', 'Both Single and Double Occupancy')]
    no = models.CharField(null=True, max_length=5)
    name = models.CharField(null=True, max_length=10)
    room_type = models.CharField(null=True, choices=room_choice, max_length=1, default=None)
    vacant = models.BooleanField(null=True, default=False)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE, null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Hostel(models.Model):
    name = models.CharField(null=True, max_length=100)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    course = models.ManyToManyField('Course', default=None, blank=True)
    caretaker = models.CharField(null=True, max_length=100, blank=True)

    def __str__(self):
        return self.name



class Course(models.Model):
    # if a student has enrollment number iit2017001 then the course code is iit2017
    code = models.CharField(null=True, max_length=100, default=None)
    room_choice = [('S', 'Single Occupancy'), ('D', 'Double Occupancy'), ('P', 'Reserved for Research Scholars'), ('B', 'Both Single and Double Occupancy')]
    room_type = models.CharField(null=True, choices=room_choice, max_length=1, default='D')

    def __str__(self):
        return self.code


# class Faculty(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)



# class Faculty(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)


#     def __str__(self):
#         return self.name


# class Department(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     faculty = models.ForeignKey('faculty', null=True, on_delete=models.CASCADE)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
    
#     def __str__(self):
#         return self.name


class Warden(models.Model):
    user = models.OneToOneField(
        User,
        default=None,
        null=True,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    hostel = models.ForeignKey('Hostel',
        default=None,
        null=True,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name



# class Bed(models.Model):
#     bed_no = models.CharField(max_length=100, 
#     null=True)
#     hostel = models.ForeignKey('hostel', null=True, on_delete= models.CASCADE)
#     # display rooms related to the selected hostel above
#     room = models.CharField(max_length=200, null=True)
    
#     date_created = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return self.bed_no




# class Allocate(models.Model):
#     status_choice = [
#         ('Pending', 'Pending'),
#         ('Approved', 'Approved'),
#         ('Rejected', 'Rejected'),
#     ]
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     status = models.CharField(choices=status_choice, null=True, max_length=100)
#     # student = models.ForeignKey('Student', null=True, on_delete=models.SET_NULL)
#     # room = models.OneToOneField('Room', null=True, on_delete=models.SET_NULL)

#     def __str__(self):
#         return self.status


# class Apply(models.Model):

#     room = models.ForeignKey('Room', default=None, null=True, on_delete=models.CASCADE)
#     checkIn = models.DateField(null=True)
#     CheckOut = models.DateField(null=True)
#     student = models.ForeignKey("Student", default=None, null=True, on_delete=models.CASCADE)
#     room_alloted = models.BooleanField(default=False)
#     accepted = models.BooleanField(default=False)
#     rejected = models.BooleanField(default=False)

#     class Meta:
#         verbose_name_plural = 'Application'

#     def __str__(self):
#         return str(self.id)

# class Leave(models.Model):
#     student = models.ForeignKey('Student', on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     reason = models.CharField(max_length=100,blank = False)
#     accept = models.BooleanField(default=False)
#     reject = models.BooleanField(default=False)
#     confirm_time = models.DateTimeField(auto_now_add=True)
