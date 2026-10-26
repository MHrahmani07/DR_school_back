from rest_framework import serializers
from .models import SMSTemplate, SMSLog

class SMSTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSTemplate
        fields = '__all__'

class SMSLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSLog
        fields = '__all__'
        read_only_fields = ('status', 'provider_response', 'created_at', 'recipient', 'message')