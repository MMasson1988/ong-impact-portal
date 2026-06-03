from django.db import models

class Report(models.Model):
    class ReportType(models.TextChoices):
        ANNUAL    = 'annual',    'Rapport annuel'
        TRIMESTER = 'trimester', 'Rapport trimestriel'
        ACTIVITY  = 'activity',  'Rapport d activite'
        FINANCIAL = 'financial', 'Rapport financier'
    title       = models.CharField(max_length=255)
    program     = models.ForeignKey('programs.Program', on_delete=models.SET_NULL, null=True, blank=True)
    report_type = models.CharField(max_length=20, choices=ReportType.choices)
    file        = models.FileField(upload_to='reports/%Y/', blank=True, null=True)
    summary     = models.TextField(blank=True)
    period      = models.CharField(max_length=50)
    is_public   = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.title} ({self.period})'
    class Meta: ordering = ['-created_at']
