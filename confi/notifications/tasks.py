from celery import shared_task
from .models import SMSLog
import time

@shared_task
def send_sms_async(recipient_phone, message_text, content_type_id=None, object_id=None):
    try:
        # شبیه‌سازی تاخیر شبکه
        time.sleep(2) 
        provider_response = "پیامک با موفقیت به مخابرات ارسال شد (شبیه‌سازی)"
        status = 'sent'
    except Exception as e:
        provider_response = str(e)
        status = 'failed'

    # استفاده از نام فیلدهای صحیح
    SMSLog.objects.create(
        recipient_phone=recipient_phone,
        message_text=message_text,
        status=status,
        provider_response=provider_response,
        content_type_id=content_type_id,
        object_id=object_id
    )
    
    return f"SMS to {recipient_phone} - Status: {status}"
