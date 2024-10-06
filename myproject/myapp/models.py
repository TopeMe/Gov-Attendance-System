from django.db import models

class Department(models.Model):
    DEPARTMENT_CHOICES = (
        ("CITY_ACCOUNTANT", "CITY ACCOUNTANT'S OFFICE"),
        ("CITY_AGRICULTURE", "CITY AGRICULTURE OFFICE"),
        ("CITY_ASSESSOR", "CITY ASSESSOR'S OFFICE"),
        ("CITY_BUDGET", "CITY BUDGET OFFICE"),
        ("CITY_ENGINEERING", "CITY ENGINEERING OFFICE"),
        ("CITY_GENERAL_SERVICES", "CITY GENERAL SERVICES OFFICE"),
        ("CITY_HEALTH", "CITY HEALTH DEPARTMENT"),
        ("CITY_TREASURER", "CITY TREASURER'S OFFICE"),
        ("CITY_DISASTER_RRM", "CITY DISASTER RRM OFFICE"),
        ("ORMOC_WATERWORKS", "ORMOC WATERWORKS OFFICE"),
        ("SPORTS", "SPORTS OFFICE"),
    )

    department_name = models.CharField(
        max_length=100,
        choices=DEPARTMENT_CHOICES,
        default="CITY_ACCOUNTANT"
    )

    def __str__(self):
        return self.get_department_name_display()

class Employee(models.Model):
    employee_id = models.CharField(max_length=50, unique=True, default='12345')  # Set a sensible default
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"





# class Attendance(models.Model):
#     STATUS_CHOICES = (
#         ("PRESENT", "Present"),
#         ("ABSENT", "Absent"),
#         ("LATE", "Late"),
#     )

#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
#     check_in = models.DateTimeField()
#     check_out = models.DateTimeField(null=True, blank=True)
#     date = models.DateField()
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES)

#     def __str__(self):
#         return f"{self.employee.name} - {self.date} - {self.status}"


# class AttendanceRecord(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_records')
#     attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='attendance_records')
#     record_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"Record for {self.employee.name} on {self.attendance.date}"