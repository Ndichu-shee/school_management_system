from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serializers import CourseSerializer, StudentSerializer, TrainerSerializer
from student.models import Student
from trainer.models import Trainer
from course.models import Course


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer