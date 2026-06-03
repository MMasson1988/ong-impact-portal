from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

class Program(models.Model):
    class Status(models.TextChoices):
        ACTIVE    = 'active',    _('Actif')
        COMPLETED = 'completed', _('Termine')
        PLANNED   = 'planned',   _('Planifie')
        ON_HOLD   = 'on_hold',   _('En pause')
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    objectives  = models.TextField(blank=True)
    status      = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    start_date  = models.DateField()
    end_date    = models.DateField(null=True, blank=True)
    budget      = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    cover_image = models.ImageField(upload_to='programs/covers/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_public   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self): return self.title
    class Meta: ordering = ['-created_at']

class Project(models.Model):
    program     = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='projects')
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    location    = models.CharField(max_length=200, blank=True)
    beneficiaries_count = models.PositiveIntegerField(default=0)
    start_date  = models.DateField()
    end_date    = models.DateField(null=True, blank=True)
    is_public   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self): return self.title
    class Meta: ordering = ['-created_at']
