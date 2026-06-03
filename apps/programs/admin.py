from django.contrib import admin
from .models import Program, Project

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'start_date', 'is_public', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectInline]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'program', 'location', 'beneficiaries_count')
    prepopulated_fields = {'slug': ('title',)}
