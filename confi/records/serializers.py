from rest_framework import serializers
from .models import Attendance, DisciplineRecord

class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.__str__', read_only=True)
    academic_year_name = serializers.CharField(source='academic_year.title', read_only=True)

    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ('created_by',)

class DisciplineRecordSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.__str__', read_only=True)
    academic_year_name = serializers.CharField(source='academic_year.title', read_only=True)

    class Meta:
        model = DisciplineRecord
        fields = '__all__'
        read_only_fields = ('created_by',)