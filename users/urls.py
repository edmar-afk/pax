from django.urls import path
from . import views

urlpatterns = [
    path('responses', views.responses, name='responses'),
    path('inquiries', views.inquiries, name='inquiries'),
    path('entryStudent', views.entryStudent, name='entryStudent'),
    path('confirmAccount', views.confirmAccount, name='confirmAccount'),
    path('mainLogin', views.mainLogin, name='mainLogin'),
    path('mainDashboard', views.mainDashboard, name='mainDashboard'),
    
    path('<int:response_id>/deleteResponse/', views.deleteResponse, name='deleteResponse'),
    path('<int:inquiry_id>/deleteInquiry/', views.deleteInquiry, name='deleteInquiry'),
    path('<int:student_id>/updateStudent/', views.updateStudent, name='updateStudent'),
    path('<int:student_id>/removeStudent/', views.removeStudent, name='removeStudent'),
    path('<int:user_id>/removeUser/', views.removeUser, name='removeUser'),
    path('acceptUser/<int:user_id>/', views.acceptUser, name='acceptUser'),
    path('declineUser/<int:user_id>/', views.declineUser, name='declineUser'),
    path('present/<int:student_id>/<int:parent_id>/', views.present, name='present'),
    path('absent/<int:student_id>/<int:parent_id>/', views.absent, name='absent'),
    
    path('login', views.login, name='login'),
    path('homepage', views.homepage, name='homepage'),
    path('register', views.register, name='register'),

    path('inquire', views.inquire, name='inquire'),
    path('inquireTeacher', views.inquireTeacher, name='inquireTeacher'),
    path('responseTeacher', views.responseTeacher, name='responseTeacher'),
    path('parentDashboard', views.parentDashboard, name='parentDashboard'),
    
    path('logoutUser', views.logoutUser, name='logoutUser'),
]