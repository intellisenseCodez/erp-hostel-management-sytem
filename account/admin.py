from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Warden)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Hostel)
admin.site.register(Room)
admin.site.register(Allocate)
# admin.site.register(Course)
admin.site.register(Bed)
admin.site.register(Leave)