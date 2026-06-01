from django.contrib import admin

from .models import Indicator, Program


class IndicatorInline(admin.TabularInline):
    model = Indicator
    extra = 1


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "sector", "region", "is_published", "is_featured")
    list_filter = ("is_published", "is_featured", "sector")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [IndicatorInline]


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ("label", "value", "unit", "program", "is_public", "is_featured")
    list_filter = ("is_public", "is_featured", "program")
