from django.contrib import admin
from .models import Attendance, DisciplineRecord

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'academic_year') 
    list_filter = ('date', 'academic_year')
    search_fields = ('student__first_name', 'student__last_name', 'student__national_id')

@admin.register(DisciplineRecord)
class DisciplineRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'academic_year') 
    list_filter = ('academic_year',)
    search_fields = ('student__first_name', 'student__last_name', 'student__national_id')