from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
import pandas as pd
# from rest_framework.decorators import action 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


def export_students_to_excel(request):
    if request.method == "GET":
        students = Student.objects.all()
        student_data = {
            'Name': [student.name for student in students],
            'Roll Number': [student.roll_number for student in students],
            # Add more fields as needed
        }
        df = pd.DataFrame(student_data)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="students.xlsx"'
        df.to_excel(response, index=False)
        return response
