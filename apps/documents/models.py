from django.db import models

class DocumentCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    def __str__(self): return self.name

class Document(models.Model):
    class AccessLevel(models.TextChoices):
        PUBLIC       = 'public',       'Public'
        PARTNER      = 'partner',      'Partenaires'
        STAFF        = 'staff',        'Staff seulement'
        CONFIDENTIAL = 'confidential', 'Confidentiel'
    title        = models.CharField(max_length=255)
    file         = models.FileField(upload_to='documents/%Y/%m/')
    category     = models.ForeignKey(DocumentCategory, on_delete=models.SET_NULL, null=True)
    access_level = models.CharField(max_length=20, choices=AccessLevel.choices, default=AccessLevel.STAFF)
    description  = models.TextField(blank=True)
    version      = models.CharField(max_length=20, default='1.0')
    uploaded_by  = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    download_count = models.PositiveIntegerField(default=0)
    def __str__(self): return self.title
    class Meta: ordering = ['-created_at']
