from django.db import models
from school.models import Student, ClassRoom, AcademicYear


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name='attendance_records')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    recorded_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'date')  # هر دانش‌آموز فقط یه رکورد غیبت در روز

    def __str__(self):
        return f"غیبت {self.student} - {self.date}"


class DisciplineRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='discipline_records')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='discipline_records')
    description = models.TextField()
    recorded_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"مورد انضباطی {self.student} - {self.created_at.date()}"