from django.http import HttpResponse
from django.shortcuts import render, redirect    
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Department

User = get_user_model()
user = User.objects.get(username='admin')  # Replace with your username
print(user.password)  # This will show a hash, confirming the user exists.


def checkin(request):
    if request.method == 'POST':
        name = request.POST.get("employee_name")
        print(name)
    return render(request, 'checkin.html')

def checkout(request):
    return render(request, 'checkout.html')



@login_required
def admin_dashboard_view(request):
    return render(request, 'admin_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Attempting login with Username: {username}")  # Log only the username for security
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(f"User {username} logged in successfully.")  # Success message
            return redirect('admin_dashboard')
        else:
            print("Login failed")  # Debugging
            return HttpResponse("Invalid login credentials. Please try again.")
    
    if request.user.is_authenticated:
        return redirect('admin_dashboard')

    return render(request, 'login.html')

@login_required
def departments(request):
    return render(request, 'departments.html')

@login_required
def reports(request):
    return render(request, 'reports.html')

@login_required
def add_employee(request):
    departments = Department.DEPARTMENT_CHOICES
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get('lastName')
        print(last_name)
    context = {
        "departments" : departments 
    }
    
    #department 1
    #departmentOne = Department.objects.filter(department_name="depOne")
    #checkins = Emplo
    return render(request, 'add_employee.html', context)

@login_required
def attendance_record(request):
    return render(request, 'attendance_record.html')

def employee_registration_view(request):
    departments = Department.objects.all()  # Fetch all departments
    return render(request, 'add_employee.html', {'departments': departments})