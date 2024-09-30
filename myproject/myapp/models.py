from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    parent_department = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_departments')

    def __str__(self):
        return self.name


# Employee Model
#class Employee(models.Model):
   # employee_id = models.CharField(max_length=10, unique=True)
   # first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)
    #department = models.ForeignKey(Department, on_delete=models.CASCADE)

    #def __str__(self):
        #return f"{self.last_name}, {self.first_name} ({self.employee_id})"


