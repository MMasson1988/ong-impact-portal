from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'report_type', 'program', 'period', 'is_public')
    list_filter  = ('report_type', 'is_public', 'program')
