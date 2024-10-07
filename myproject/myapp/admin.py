from django.contrib import admin
from .models import Department, Employee

# @admin.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     list_display = ('department_name',) 

# # @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ('employee_id', 'first_name', 'last_name', 'department')  # Update to match the new fields
