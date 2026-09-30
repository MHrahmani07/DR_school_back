from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class SMSTemplate(models.Model):
    key = models.CharField(max_length=30, unique=True)   # مثلاً "absence", "discipline"
    text = models.TextField()   # می‌تونه {student_name} و امثالش داشته باشه

    def __str__(self):
        return self.key


class SMSLog(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'در صف'
        SENT = 'sent', 'ارسال شده'
        FAILED = 'failed', 'ناموفق'

    recipient_phone = models.CharField(max_length=15)
    message_text = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    provider_response = models.TextField(blank=True)
    sent_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    # اتصال اختیاری به یک Attendance یا DisciplineRecord یا هیچ‌کدام (پیامک همگانی)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    related_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.recipient_phone} - {self.status}"