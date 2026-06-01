from django.contrib import admin

from .models import DashboardWidget


@admin.register(DashboardWidget)
class DashboardWidgetAdmin(admin.ModelAdmin):
    list_display = ("title", "widget_type", "order", "is_active")
    list_filter = ("widget_type", "is_active")
