from django.contrib import admin
from .models import AcademicYear, GradeLevel, ClassRoom, Student

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_current', 'start_date', 'end_date')
    list_filter = ('is_current',)
    search_fields = ('title',)

@admin.register(GradeLevel)
class GradeLevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)
    search_fields = ('title',)

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade_level', 'academic_year', 'class_type', 'supervisor')
    list_filter = ('academic_year', 'grade_level', 'class_type')
    search_fields = ('name',)
    autocomplete_fields = ('supervisor',) # اگر در accounts/admin.py برای User فیلد search_fields تعریف کرده باشی کاربردی است

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'national_id', 'parent_phone', 'classroom', 'status')
    list_filter = ('status', 'classroom__academic_year', 'classroom__grade_level', 'classroom')
    search_fields = ('first_name', 'last_name', 'national_id', 'father_name', 'parent_phone')
    readonly_fields = ('created_at',)