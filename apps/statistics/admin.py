from django.contrib import admin
from .models import Indicator, KeyStat

@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'program', 'current', 'target', 'period')

@admin.register(KeyStat)
class KeyStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'order', 'is_active')
