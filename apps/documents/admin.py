from django.contrib import admin

from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "document_type", "is_published", "is_private", "program")
    list_filter = ("document_type", "is_published", "is_private", "program")
    search_fields = ("title", "summary")
