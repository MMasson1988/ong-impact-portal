from django.db import models


class DashboardWidget(models.Model):
    """Widget configurable pour tableaux de bord staff."""

    class WidgetType(models.TextChoices):
        KPI = "kpi", "Indicateur clé"
        CHART = "chart", "Graphique (placeholder)"
        LIST = "list", "Liste"
        TEXT = "text", "Texte"

    title = models.CharField(max_length=120)
    widget_type = models.CharField(max_length=20, choices=WidgetType.choices, default=WidgetType.KPI)
    config_json = models.JSONField(default=dict, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "widget tableau de bord"

    def __str__(self):
        return self.title
