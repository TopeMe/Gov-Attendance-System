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
        default="CITY_ACCOUNTANT"  # Use the correct key from DEPARTMENT_CHOICES
    )

    def __str__(self):
        return self.get_department_name_display()



# Employee Model
class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
  
    


