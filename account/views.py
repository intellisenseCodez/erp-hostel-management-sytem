from multiprocessing import context
from unicodedata import name
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .decorators import unauthenticated_user, allowed_users, admin_only


from .models import *
from .forms import *

# Create your views here.
# @unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR Password is incorrect!')

    context = {}
    return render(request, 'account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

# @unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='student')
            user.groups.add(group)

            Student.objects.create(user=user)

            # send flash message
            messages.success(request, "Account was successfully created for " + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html', context)


@login_required(login_url="login")
@admin_only
def home(request):
    students = Student.objects.all()
    rooms = Room.objects.all()
    hostels = Hostel.objects.all()
    wardens = Warden.objects.all()
    context = {"students": students, "rooms": rooms, "hostels": hostels, "wardens": wardens}
    return render(request, 'account/dashboard.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def hostels(request):
    hostels = Hostel.objects.all()
    context = {"hostels": hostels}
    return render(request, 'account/hostel/all.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def hostelSingle(request, pk):
    hostel = Hostel.objects.get(id=pk)
    context = {"hostel": hostel}
    return render(request, 'account/hostel/view.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def createHostel(request):
    hostel_form = HostelForm()

    if request.method == 'POST':
        hostel_form = HostelForm(request.POST)
        if hostel_form.is_valid:
            hostel_form.save()
            return redirect("/hostels/")

    context = {'hostel_form': hostel_form}
    return render(request, 'account/hostel/add.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def updateHostel(request, pk):
    hostel = Hostel.objects.get(id=pk)
    hostel_form = HostelForm(instance=hostel)

    if request.method == 'POST':
        hostel_form = HostelForm(request.POST, instance=hostel)
        if hostel_form.is_valid:
            hostel_form.save()
            return redirect("/hostels/")

    context = {'hostel_form': hostel_form}
    return render(request, 'account/hostel/add.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def deleteHostel(request, pk):
    hostel_info = Hostel.objects.get(id=pk)

    if request.method == 'POST':
        hostel_info.delete()
        return redirect("/hostels/")

    context = {'hostel_info': hostel_info}
    return render(request, 'account/hostel/delete.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def wardens(request):
    wardens = Warden.objects.all()
    context = {"wardens": wardens}
    return render(request, 'account/warden/all.html', context)


@allowed_users(allowed_roles=['admin',])
def wardenSingle(request, pk):
    warden = Warden.objects.get(id=pk)
    context = {"warden": warden}
    return render(request, 'account/warden/view.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def createWarden(request):
    warden_form = WardenForm()

    if request.method == 'POST':
        warden_form = WardenForm(request.POST)
        if warden_form.is_valid:
            warden_form.save()
            return redirect("/wardens/")

    context = {'warden_form': warden_form}
    return render(request, 'account/warden/add.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def updateWarden(request, pk):
    warden = Warden.objects.get(id=pk)
    warden_form = WardenForm(instance=warden)

    if request.method == 'POST':
        warden_form = WardenForm(request.POST, instance=warden)
        if warden_form.is_valid:
            warden_form.save()
            return redirect("/wardens/")

    context = {'warden_form': warden_form}
    return render(request, 'account/warden/add.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def deleteWarden(request, pk):
    warden_info = Warden.objects.get(id=pk)

    if request.method == 'POST':
        warden_info.delete()
        return redirect("/wardens/")

    context = {'warden_info': warden_info}
    return render(request, 'account/warden/delete.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def rooms(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, 'account/room/all.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def roomSingle(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, 'account/room/view.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def createRoom(request):
    room_form = RoomForm()

    if request.method == 'POST':
        room_form = RoomForm(request.POST)
        if room_form.is_valid:
            room_form.save()
            return redirect("/rooms/")

    context = {'room_form': room_form}
    return render(request, 'account/room/add.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    room_form = RoomForm(instance=room)

    if request.method == 'POST':
        room_form = RoomForm(request.POST, instance=room)
        if room_form.is_valid:
            room_form.save()
            return redirect("/rooms/")

    context = {'room_form': room_form}
    return render(request, 'account/room/add.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def deleteRoom(request, pk):
    room_info = Room.objects.get(id=pk)

    if request.method == 'POST':
        room_info.delete()
        return redirect("/rooms/")

    context = {'room_info': room_info}
    return render(request, 'account/room/delete.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def students(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, 'account/students/all.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def studentSingle(request, pk):
    student = Student.objects.get(id=pk)
    context = {"student": student}
    return render(request, 'account/students/view.html', context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def createStudent(request):
    student_form = StudentForm()

    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid:
            student_form.save()
            return redirect("/students/")

    context = {'student_form': student_form}
    return render(request, 'account/students/add.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    student_form = StudentForm(instance=student)

    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid:
            student_form.save()
            return redirect("/students/")

    context = {'student_form': student_form}
    return render(request, 'account/students/add.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['admin',])
def deleteStudent(request, pk):
    student_info = Student.objects.get(id=pk)

    if request.method == 'POST':
        student_info.delete()
        return redirect("/students/")

    context = {'student_info': student_info}
    return render(request, 'account/students/delete.html', context)



@login_required(login_url="login")
@allowed_users(allowed_roles=['student',])
def userPage(request):
    context= {}
    return render(request, 'account/user.html', context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['student',])
def userProfile(request):
     
    student = request.user.student
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance = student)
        if form.is_valid():
            form.save()

    context= {'form': form}
    return render(request, 'account/profile.html', context)


# students
@allowed_users(allowed_roles=['student',])
def apply_for_room(request):
    if request.user.student.room:
        return HttpResponse('You have already selected room - ' + str(request.user.student.room) + '. Please contact your Hostel Caretaker or Warden')

    if request.method == 'POST':
        if not request.user.student.no_dues:
            return HttpResponse('You have dues. Please contact your Hostel Caretaker or Warden')
        
        form = SelectionForm(request.POST, instance=request.user.student)
        if form.is_valid():
            if request.user.student.room_id:
                request.user.student.room_allotted = True
                room_id = request.user.student.room_id
                room = Room.objects.get(id=room_id)
                room.vacant = False
                room.save()
            form.save()
            student = request.user.student
            return render(request, 'account/user.html', {'student': student})
    else:
        print('GOT HERE')
        if not request.user.student.no_dues:
            return HttpResponse('You have dues. Please contact your Hostel Caretaker or Warden')

        form = SelectionForm(instance=request.user.student)

        student_gender = request.user.student.gender
        student_course = request.user.student.course
        student_room_type = request.user.student.course.room_type

        print({'gender':student_gender, 'course':student_course, 'room type':student_room_type})

        hostel = Hostel.objects.filter(
            gender=student_gender, course=student_course)
        
        # returning zero number of hostels
        print("Hostels: " ,hostel)

        filtered_rooms = Room.objects.none()
        print(filtered_rooms)
        print("I'm here before cond.")
        if student_room_type == 'B':
            print("I'm here #1")
            for i in range(len(hostel)):
                h_id = hostel[i].id
                filtered_room = Room.objects.filter(
                    hostel_id=h_id, room_type=['S', 'D'], vacant=True)
                filtered_rooms = filtered_rooms | filtered_room
        else :
            print("I'm here Room type is not B")
            for i in range(len(hostel)):
                length = len(hostel)
                print(length)
                h_id = hostel[i].id
                print(h_id)
                filtered_room = Room.objects.filter(
                    hostel_id=h_id, room_type=student_room_type, vacant=True)
                
                print(filtered_room)

                filtered_rooms = filtered_rooms | filtered_room

                
                print(filtered_rooms)

        form.fields["room"].queryset = filtered_rooms
        return render(request, 'account/apply_for_room.html', {'form': form})
