from django.contrib import admin
from .models import RolloverLog



@admin.register(RolloverLog)
class RolloverLogAdmin(admin.ModelAdmin):
    list_display = ('from_year', 'to_year')
