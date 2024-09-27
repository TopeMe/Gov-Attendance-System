from django.db import models

# Department Model
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    total_employees = models.IntegerField(default=0)
    total_present = models.IntegerField(default=0)
    total_absent = models.IntegerField(default=0)
    total_late = models.IntegerField(default=0)

    def __str__(self):
        return self.department_name

# Employee Model
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Attendance Record Model
class AttendanceRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    arrival_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='attendance_records')

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

# Daily Summary Report Model
class DailySummaryReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    date = models.DateField()
    total_attended = models.IntegerField(default=0)
    total_absent = models.IntegerField(default=0)
    total_late = models.IntegerField(default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='daily_reports')

    def __str__(self):
        return f"{self.department.department_name} - {self.date}"
