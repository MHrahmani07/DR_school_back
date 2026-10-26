from rest_framework import serializers
from .models import AcademicYear, GradeLevel, ClassRoom, Student

class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = '__all__'

class GradeLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeLevel
        fields = '__all__'

class ClassRoomSerializer(serializers.ModelSerializer):
    # برای نمایش نام سال و پایه در خروجی (علاوه بر ID)
    academic_year_name = serializers.CharField(source='academic_year.title', read_only=True)
    grade_level_name = serializers.CharField(source='grade_level.title', read_only=True)

    class Meta:
        model = ClassRoom
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    classroom_name = serializers.CharField(source='classroom.name', read_only=True)

    class Meta:
        model = Student
        fields = '__all__'