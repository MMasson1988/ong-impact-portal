from django.db import models

class Indicator(models.Model):
    program    = models.ForeignKey('programs.Program', on_delete=models.CASCADE, related_name='indicators')
    name       = models.CharField(max_length=200)
    unit       = models.CharField(max_length=50)
    target     = models.FloatField()
    current    = models.FloatField(default=0)
    period     = models.CharField(max_length=10)
    is_public  = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    @property
    def progress_pct(self):
        return round((self.current / self.target) * 100, 1) if self.target else 0
    def __str__(self): return f'{self.name} ({self.period})'

class KeyStat(models.Model):
    label     = models.CharField(max_length=100)
    value     = models.CharField(max_length=50)
    icon      = models.CharField(max_length=50, blank=True)
    order     = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    def __str__(self): return self.label
    class Meta: ordering = ['order']
