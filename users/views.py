from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth import authenticate, login as auth_login
from .models import Student, Attendance, ResponseNotes, InquireNotes
from django.utils import timezone
from datetime import datetime, timedelta
# Create your views here.

def responses(request):
    notes = ResponseNotes.objects.all().order_by('-id')
    
    context = {
        'notes': notes,
    }
    
    return render(request, 'main/responses.html', context)

def inquiries(request):
    inquiries = InquireNotes.objects.all().order_by('-id')
    
    context = {
        'inquiries': inquiries,
    }
    
    return render(request, 'main/inquiry.html', context)


def entryStudent(request):
    users = User.objects.all().order_by('-id')
    
    if request.method == 'POST':
        student = request.POST['student']
        parent_id = request.POST['parents']
        parent = get_object_or_404(User, id=parent_id)
        
        new_student = Student.objects.create(name=student, parent=parent)
        new_student.save()
        messages.success(request, 'Student Successfully added')
    
    context = {
        'users': users
    }
    
    return render(request, 'main/entryStudent.html', context)

def confirmAccount(request):
    parents = User.objects.all().order_by('-id')
    
    context = {
        'parents': parents
    }
    
    return render(request, 'main/confirmAccount.html', context)


def mainResponse(request):
    notes = ResponseNotes.objects.all().order_by('-d')
   
    context = {
        'notes':notes
    }
    
    return render(request, 'main/index.html', context)


def mainLogin(request):
    return render(request, 'main/mainLogin.html')

def mainDashboard(request):
    students = Student.objects.all().order_by('-id')
    parents = User.objects.all().order_by('-id')
   
    context = {
        'students': students,
        'parents': parents,
    }
    
    return render(request, 'main/index.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        info = authenticate(username=email, password=password)
        if info is not None:
            auth_login(request, info)
            if info.is_staff and info.last_name == 'Parent':
                return redirect('parentDashboard')
            else:
                messages.error(request, "You are not approve to the admin. Please wait")
                return redirect('login')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login')
    return render(request, 'login.html')
    
def homepage(request):
    
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        address = request.POST['address']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'School Id already taken.')
                return redirect('register')

            else:
                new_student = User.objects.create_user(
                    first_name=fullname, username=email, password=password1,last_name='Parent', email=address, is_staff=False, is_superuser=False )
                new_student.save()
                messages.success(request, 'Account created')
                return redirect('login')
        else:
            messages.error(request, 'Password does not match.')
            return redirect('register')
    return render(request, 'register.html')


def inquireTeacher(request):
    
    if request.method == 'POST':
        note = request.POST['response']
        
        new_response = ResponseNotes.objects.create(sender=request.user, notes=note, date_submitted=timezone.now())
        new_response.save()
        messages.success(request, 'Response sent')
    context = {
        
    }
    
    return render(request, 'parent/inquire.html', context)


def responseTeacher(request):
    students = Student.objects.all().order_by('-id')
    parents = User.objects.all().order_by('-id')
    
    if request.method == 'POST':
        note = request.POST['response']
        
        new_response = ResponseNotes.objects.create(sender=request.user, notes=note, date_submitted=timezone.now())
        new_response.save()
        messages.success(request, 'Response sent')
    context = {
        'students': students,
        'parents': parents,
    }
    
    return render(request, 'parent/response.html', context)


def parentDashboard(request):
    attendance = Attendance.objects.filter(parent=request.user).order_by('-id')
    
    context = {
        'attendance': attendance
    }
    return render(request, 'parent/index.html', context)



def removeUser(request, user_id):
    User.objects.filter(id=user_id).delete()
    messages.success(request, 'User Removed')
    return redirect(request.META.get('HTTP_REFERER'))

def deleteInquiry(request, inquiry_id):
    InquireNotes.objects.filter(id=inquiry_id).delete()
    messages.success(request, 'Inquiry Removed')
    return redirect(request.META.get('HTTP_REFERER'))


def deleteResponse(request, response_id):
    ResponseNotes.objects.filter(id=response_id).delete()
    messages.success(request, 'Feedback Removed')
    return redirect(request.META.get('HTTP_REFERER'))


def removeStudent(request, student_id):
    Student.objects.filter(id=student_id).delete()
    messages.success(request, 'Student Removed')
    return redirect(request.META.get('HTTP_REFERER'))

def acceptUser(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_staff = True
    user.save()
    # You can redirect to a success page or to the same page
    messages.success(request, 'User Accepted')
    return redirect(request.META.get('HTTP_REFERER'))

def declineUser(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_staff = False
    user.save()
    # You can redirect to a success page or to the same page
    messages.success(request, 'User Declined')
    return redirect(request.META.get('HTTP_REFERER'))

def logoutUser(request):
    auth.logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('homepage')


def updateStudent(request, student_id):
    student = Student.objects.get(pk=student_id)
    
    if request.method == 'POST':
        
        name = request.POST['student']
        parent_id = request.POST['parents']
        
        parent = get_object_or_404(User, id=parent_id)
        student.name = name
        student.parent = parent
        student.save()
    
    messages.success(request, 'Student info Updated')
    return redirect(request.META.get('HTTP_REFERER'))


def present(request, student_id, parent_id):
    student = get_object_or_404(Student, pk=student_id)
    parent = get_object_or_404(User, pk=parent_id)
    
    # Get the start and end of the current day
    today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = today_start + timedelta(days=1)
    
    # Check if an attendance record already exists for today
    existing_attendance = Attendance.objects.filter(
        student=student,
        parent=parent,
        attended_at__range=(today_start, today_end)
    ).exists()
    
    if existing_attendance:
        messages.warning(request, f'Attendance has already been marked for {student.name} today.')
    else:
        Attendance.objects.create(student=student, parent=parent, status='Present', attended_at=timezone.now())
        messages.success(request, f'Attendance marked for {student.name}!')
    
    return redirect(request.META.get('HTTP_REFERER'))




def absent(request, student_id, parent_id):
    student = get_object_or_404(Student, pk=student_id)
    parent = get_object_or_404(User, pk=parent_id)
    
    # Get the start and end of the current day
    today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = today_start + timedelta(days=1)
    
    # Check if an attendance record already exists for today
    existing_attendance = Attendance.objects.filter(
        student=student,
        parent=parent,
        attended_at__range=(today_start, today_end)
    ).exists()
    
    if existing_attendance:
        messages.warning(request, f'Attendance has already been marked for {student.name} today.')
    else:
        Attendance.objects.create(student=student, parent=parent, status='Absent', attended_at=timezone.now())
        messages.success(request, f'Attendance marked for {student.name}!')
    
    return redirect(request.META.get('HTTP_REFERER'))


def inquire(request):
    eight_hours_ago = timezone.now() - timedelta(hours=8)
    last_inquiry = InquireNotes.objects.filter(sender=request.user).order_by('-date_submitted').first()
    
    if last_inquiry and last_inquiry.date_submitted > eight_hours_ago:
        messages.error(request, "You can only submit an inquiry once every 8 hours. Don't worry, the teacher will surely recieved your request")
    else:
        new_inquiry = InquireNotes.objects.create(sender=request.user, 
                                                  notes='Requesting to check on their Children', 
                                                  date_submitted=timezone.now())
        new_inquiry.save()
        messages.success(request, 'Request Submitted')
    
    return redirect(request.META.get('HTTP_REFERER'))