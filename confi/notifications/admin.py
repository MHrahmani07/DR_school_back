from django.contrib import admin
from .models import SMSTemplate, SMSLog

@admin.register(SMSTemplate)
class SmsTemplateAdmin(admin.ModelAdmin):
    list_display=()