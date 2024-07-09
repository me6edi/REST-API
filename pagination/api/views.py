from django.shortcuts import render # type: ignore
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView # type: ignore
# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer