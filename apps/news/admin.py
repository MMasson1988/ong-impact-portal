from django.contrib import admin
from .models import NewsArticle

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'audience', 'is_published', 'published_at', 'author')
    list_filter  = ('audience', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
