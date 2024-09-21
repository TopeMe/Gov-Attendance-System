from django.http import HttpResponse
from django.shortcuts import render, redirect    
from django.contrib.auth.decorators import login_required

def punch_page(request):
    if request.method == 'POST':
        name = request.POST.get("employee_name")
        print(name)
    return render(request, 'punch.html')


@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


def departments(request):
    return render(request, 'departments.html')

def add_employee(request):
    return render(request, 'add_employee.html')


def admin_dashboard(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request, 'admin_dashboard.html')
        else:
            return HttpResponse("Invalid login credentials. Please try again.")
    
    return render(request, 'punch.html')  # This will show the login form initially
    
