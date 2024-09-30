from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)




#@admin.register(Employee)
#class EmployeeAdmin(admin.ModelAdmin):
    #list_display = ('employee_id', 'first_name', 'last_name', 'department')
