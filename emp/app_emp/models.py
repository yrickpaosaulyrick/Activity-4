from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length = 100)
    salary= models.FloatField()
    age = models.IntegerField()
    birthday = models.DateField()
    remarks = models.TextField()

    class Meta:
        db_table = 'Employee_List'
