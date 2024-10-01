from django.db import models

class Department(models.Model):
    DEPARTMENT_CHOICES = (
        ("JANUARY", "January"),
        ("FEBRUARY", "February"),
        ("MARCH", "March"),
        # ....
        ("DECEMBER", "December"),
    )

    department_name = models.CharField(max_length=100, choices= DEPARTMENT_CHOICES, default="JANUARY")

    def __str__(self):
        return self.name


# Employee Model
class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
  
    


