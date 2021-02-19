from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from school.models import School, Student
from school.serializer import SchoolSerializers, StudentSerializers


class SchoolList(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializers


class SchoolDetails(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return School.objects.filter(id=self.kwargs.get('pk', None))

    serializer_class = SchoolSerializers


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Student.objects.filter(id=self.kwargs.get('pk', None))

    serializer_class = StudentSerializers
