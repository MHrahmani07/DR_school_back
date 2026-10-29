from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Attendance
from notifications.tasks import send_sms_async

@receiver(post_save, sender=Attendance)
def trigger_attendance_sms(sender, instance, created, **kwargs):
    if created: # فقط وقتی غیبت جدیدی ساخته میشه (نه موقع ویرایش)
        
        # شماره موبایل والد و نام دانش‌آموز رو می‌گیریم
        parent_phone = instance.student.parent_phone
        student_name = f"{instance.student.first_name} {instance.student.last_name}"
        
        # متن پیامک رو می‌سازیم (بعدا میشه از SMSTemplate خوند)
        message = f"ولی محترم، غیبت دانش‌آموز {student_name} در تاریخ {instance.date} در سیستم ثبت گردید."
        
        # آیدی مدل برای لاگ کردن پیامک
        content_type_id = ContentType.objects.get_for_model(instance).id
        
        # delay 
        send_sms_async.delay(
            recipient_phone=parent_phone,  
            message_text=message,
            content_type_id=content_type_id,
            object_id=instance.id
        )