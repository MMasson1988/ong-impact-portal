from django.db import models

class Album(models.Model):
    title       = models.CharField(max_length=200)
    program     = models.ForeignKey('programs.Program', on_delete=models.SET_NULL, null=True, blank=True)
    cover       = models.ImageField(upload_to='gallery/covers/', blank=True, null=True)
    description = models.TextField(blank=True)
    is_public   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title

class Photo(models.Model):
    album      = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    image      = models.ImageField(upload_to='gallery/photos/%Y/%m/')
    caption    = models.CharField(max_length=255, blank=True)
    taken_at   = models.DateField(null=True, blank=True)
    uploaded_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.caption or f'Photo {self.pk}'
