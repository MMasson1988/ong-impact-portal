from django.db import models


class SiteSettings(models.Model):
    """Paramètres globaux du portail (singleton)."""

    site_name = models.CharField("Nom du site", max_length=120, default="ONG Impact Portal")
    tagline = models.CharField("Slogan", max_length=255, blank=True)
    mission = models.TextField("Mission", blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)

    class Meta:
        verbose_name = "paramètres du site"
        verbose_name_plural = "paramètres du site"

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class InstitutionalPage(models.Model):
    """Pages institutionnelles publiques (À propos, Gouvernance, etc.)."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField(blank=True)
    body = models.TextField()
    is_published = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "page institutionnelle"

    def __str__(self):
        return self.title
