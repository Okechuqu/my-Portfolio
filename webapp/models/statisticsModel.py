from django.db import models

class Statistics(models.Model):
    
    name = models.CharField(max_length=250, blank=True, null=True)
    icon = models.CharField(max_length=150, blank=True, null=True)
    stats_numb = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'stat'
        verbose_name_plural = 'statistics'
