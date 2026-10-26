from django.contrib import admin
from .models import SMSTemplate, SMSLog

@admin.register(SMSTemplate)
class SMSTemplateAdmin(admin.ModelAdmin):
    list_display = ('key', 'preview_text')

    @admin.display(description='متن پیامک')
    def preview_text(self, obj):
        return obj.text[:50]

@admin.register(SMSLog)
class SMSLogAdmin(admin.ModelAdmin):
    list_display = (
        'recipient_phone',
        'status',
        'sent_by',
        'sent_at',
    )


    list_filter = ('status', 'sent_at')
    search_fields = ('recipient_phone', 'message_text')
    readonly_fields = ('sent_at',)