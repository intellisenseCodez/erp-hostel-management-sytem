from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.home, name='dashboard'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('hostels/', views.hostels, name='hostels'),
    path('hostels/add', views.createHostel, name='create_hostel'),
    path('hostels/<str:pk>/', views.hostelSingle, name='hostel_single'),
    path('hostel/update/<str:pk>/', views.updateHostel, name='update_hostel'),
    path('hostel/delete/<str:pk>/', views.deleteHostel, name='delete_hostel'),
    
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/add', views.createRoom, name='create_room'),
    path('rooms/<str:pk>/', views.roomSingle, name='room_single'),
    path('room/update/<str:pk>/', views.updateRoom, name='update_room'),
    path('room/delete/<str:pk>/', views.deleteRoom, name='delete_room'),
  
    path('wardens/', views.wardens, name='wardens'),
    path('wardens/add', views.createWarden, name='create_warden'),
    path('wardens/<str:pk>/', views.wardenSingle, name='warden_single'),
    path('warden/update/<str:pk>/', views.updateWarden, name='update_warden'),
    path('warden/delete/<str:pk>/', views.deleteWarden, name='delete_warden'),
  
    path('students/', views.students, name='students'),
    path('students/add', views.createStudent, name='create_student'),
    path('students/<str:pk>/', views.studentSingle, name='student_single'),
    path('student/update/<str:pk>/', views.updateStudent, name='update_student'),
    path('student/delete/<str:pk>/', views.deleteStudent, name='delete_student'),
    
    # Students
    path('user/', views.userPage, name='user-page'),
    path('user/profile', views.userProfile, name='user-profile'),
    path('student/apply/room', views.apply_for_room, name="apply_for_room"),
  
]
