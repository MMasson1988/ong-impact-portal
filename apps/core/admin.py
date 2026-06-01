from django.contrib import admin

from .models import InstitutionalPage, SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(InstitutionalPage)
class InstitutionalPageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published", "order", "updated_at")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("is_published",)
