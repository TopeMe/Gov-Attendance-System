from django.http import HttpResponse
from django.shortcuts import render

def punch_page(request):
    if request.method == 'POST':
        name = request.POST.get("employee_name")
        print(name)
    return render(request, 'punch.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
    
def home(request):
    return HttpResponse("Welcome to the F System!")