from django.db import models
from school.models import AcademicYear


class RolloverLog(models.Model):
    from_year = models.ForeignKey(AcademicYear, on_delete=models.PROTECT, related_name='rollover_from')
    to_year = models.ForeignKey(AcademicYear, on_delete=models.PROTECT, related_name='rollover_to')
    performed_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    performed_at = models.DateTimeField(auto_now_add=True)
    students_promoted = models.PositiveIntegerField(default=0)
    students_graduated = models.PositiveIntegerField(default=0)
    backup_file = models.FileField(upload_to='rollover_backups/', null=True, blank=True)

    def __str__(self):
        return f"رولاور {self.from_year} → {self.to_year}"