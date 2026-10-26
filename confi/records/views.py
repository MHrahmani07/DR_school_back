from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Attendance, DisciplineRecord
from .serializers import AttendanceSerializer, DisciplineRecordSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # قابلیت فیلتر بر اساس دانش‌آموز، سال تحصیلی، تاریخ دقیق و کلاس دانش‌آموز
    filterset_fields = ['student', 'academic_year', 'date', 'student__classroom']
    ordering_fields = ['date']
    ordering = ['-date']

    def perform_create(self, serializer):
        # ذخیره خودکار کاربری که غیبت رو ثبت کرده
        serializer.save(created_by=self.request.user if self.request.user.is_authenticated else None)

class DisciplineRecordViewSet(viewsets.ModelViewSet):
    queryset = DisciplineRecord.objects.all()
    serializer_class = DisciplineRecordSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['student', 'academic_year']
    search_fields = ['description', 'student__first_name', 'student__last_name', 'student__national_id']
    ordering_fields = ['date']
    ordering = ['-date']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user if self.request.user.is_authenticated else None)