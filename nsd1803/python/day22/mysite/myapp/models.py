from django.db import models

class Department(models.Model):
    dep_name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.dep_name

class Employee(models.Model):
    emp_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    depart = models.ForeignKey(Department, models.CASCADE)
    def __str__(self):
        return self.emp_name
