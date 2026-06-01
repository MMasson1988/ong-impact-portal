from django.db import models
from django.urls import reverse


class Program(models.Model):
    """Programme ou projet ONG."""

    name = models.CharField("Nom", max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField("Résumé")
    description = models.TextField("Description")
    sector = models.CharField("Secteur", max_length=100, blank=True)
    region = models.CharField("Zone", max_length=100, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    cover_image = models.ImageField(upload_to="programs/", blank=True, null=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField("Mis en avant", default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "programme"
        verbose_name_plural = "programmes"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("programs:detail", kwargs={"slug": self.slug})


class Indicator(models.Model):
    """Indicateur de performance (KPI)."""

    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        related_name="indicators",
        null=True,
        blank=True,
    )
    label = models.CharField("Libellé", max_length=200)
    value = models.CharField("Valeur", max_length=100)
    unit = models.CharField("Unité", max_length=50, blank=True)
    period = models.CharField("Période", max_length=80, blank=True)
    is_public = models.BooleanField("Visible publiquement", default=True)
    is_featured = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_featured", "label"]
        verbose_name = "indicateur"

    def __str__(self):
        return f"{self.label}: {self.value} {self.unit}".strip()
