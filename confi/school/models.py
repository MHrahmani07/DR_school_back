from django.db import models


class AcademicYear(models.Model):
    title = models.CharField(max_length=20, unique=True)   # مثلاً "1403-1404"
    is_current = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class GradeLevel(models.Model):
    title = models.CharField(max_length=30, unique=True)   # "پایه اول" تا "پایه ششم"
    order = models.PositiveSmallIntegerField(unique=True)  # 1 تا 6 — برای منطق ارتقا لازمه

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ClassRoom(models.Model):
    class ClassType(models.TextChoices):
        GIRLS = 'girls', 'دخترانه'
        BOYS = 'boys', 'پسرانه'
        MIXED = 'mixed', 'مختلط'

    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='classrooms')
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.PROTECT, related_name='classrooms')
    name = models.CharField(max_length=50)   # مثلاً "سوم فجر ۱"
    class_type = models.CharField(max_length=10, choices=ClassType.choices)
    supervisor = models.ForeignKey(
        'accounts.User', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='supervised_classes'
    )

    class Meta:
        unique_together = ('academic_year', 'name')

    def __str__(self):
        return f"{self.name} ({self.academic_year.title})"


class Student(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'فعال'
        GRADUATED = 'graduated', 'فارغ‌التحصیل'
        TRANSFERRED = 'transferred', 'انتقالی'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50, blank=True)
    national_id = models.CharField(max_length=10, unique=True)
    parent_phone = models.CharField(max_length=15)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True, related_name='students')
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"