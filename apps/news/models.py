from django.db import models
from django.utils.text import slugify

class NewsArticle(models.Model):
    class Audience(models.TextChoices):
        PUBLIC  = 'public',  'Public'
        STAFF   = 'staff',   'Staff interne'
        PARTNER = 'partner', 'Partenaires'
    title      = models.CharField(max_length=255)
    slug       = models.SlugField(unique=True, blank=True)
    content    = models.TextField()
    excerpt    = models.TextField(blank=True, max_length=300)
    cover      = models.ImageField(upload_to='news/covers/', blank=True, null=True)
    audience   = models.CharField(max_length=20, choices=Audience.choices, default=Audience.PUBLIC)
    author     = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self): return self.title
    class Meta: ordering = ['-published_at']
