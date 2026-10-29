from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import AcademicYear, GradeLevel, ClassRoom, Student
from accounts.permissions import IsAdminOrDeputyReadOnly
from .serializers import (
    AcademicYearSerializer, GradeLevelSerializer, 
    ClassRoomSerializer, StudentSerializer
)

class AcademicYearViewSet(viewsets.ModelViewSet):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer
    permission_classes = [IsAdminOrDeputyReadOnly]   
    filterset_fields = ['is_current']

class GradeLevelViewSet(viewsets.ModelViewSet):
    queryset = GradeLevel.objects.all()
    serializer_class = GradeLevelSerializer
    permission_classes = [IsAdminOrDeputyReadOnly]
    ordering_fields = ['order']
    ordering = ['order']

class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = [IsAdminOrDeputyReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['academic_year', 'grade_level', 'class_type']
    search_fields = ['name']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrDeputyReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['classroom', 'status', 'classroom__academic_year']
    search_fields = ['first_name', 'last_name', 'national_id', 'parent_phone']
    ordering_fields = ['last_name', 'created_at']