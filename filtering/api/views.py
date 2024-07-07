from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

# Create your views here.

# Filtering in django

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # filter in django
#     # filters_fields = ['city']
#     # filters_fields = ['name','city']


# Search Filter in Django

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # Search filter
#     filter_backends = [SearchFilter]
#     # search_fields = ['name','city']
#     # search_fields = ['^name'] # '^' Starts with search any character.


# Ordering Filter
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    # ordering_fields = ['name']
    ordering_fields = ['name','city']