from django.db import models
from django.urls import reverse

from apps.programs.models import Program


class InternalNews(models.Model):
    """Actualités internes (certaines publiques, d'autres staff-only)."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    program = models.ForeignKey(
        Program, on_delete=models.SET_NULL, null=True, blank=True, related_name="news"
    )
    is_published = models.BooleanField(default=True)
    is_staff_only = models.BooleanField("Réservé au staff", default=False)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "actualité"
        verbose_name_plural = "actualités"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("content:news_detail", kwargs={"slug": self.slug})


class Achievement(models.Model):
    """Réalisation interne valorisée."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    program = models.ForeignKey(
        Program, on_delete=models.SET_NULL, null=True, blank=True, related_name="achievements"
    )
    date = models.DateField()
    is_published = models.BooleanField(default=True)
    is_staff_only = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date"]
        verbose_name = "réalisation"

    def __str__(self):
        return self.title


class Photo(models.Model):
    """Photo d'activité."""

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="photos/")
    caption = models.CharField(max_length=255, blank=True)
    program = models.ForeignKey(
        Program, on_delete=models.SET_NULL, null=True, blank=True, related_name="photos"
    )
    taken_at = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    is_staff_only = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]
        verbose_name = "photo"

    def __str__(self):
        return self.title
