from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display = ['name','last_name','roll_number','department','semester']
    