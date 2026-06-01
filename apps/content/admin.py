from django.contrib import admin

from .models import Achievement, InternalNews, Photo


@admin.register(InternalNews)
class InternalNewsAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "is_staff_only", "published_at")
    list_filter = ("is_published", "is_staff_only", "program")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", "program", "date", "is_published", "is_staff_only")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "program", "is_published", "is_staff_only", "uploaded_at")
    list_filter = ("is_published", "is_staff_only", "program")
