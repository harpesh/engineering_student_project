from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()
    phone_no = models.IntegerField()
    joinig_date = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField( max_length=254, unique=True)
    city_name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.names