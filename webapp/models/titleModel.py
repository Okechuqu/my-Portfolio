from django.db import models
from ckeditor.fields import RichTextField


class Title(models.Model):
    projectTitle = models.CharField(max_length=250, blank=True, null=True)
    projectDescribe = models.CharField(max_length=250, blank=True, null=True)
    serviceTitle = models.CharField(max_length=250, blank=True, null=True)
    contactTitle = models.CharField(max_length=250, blank=True, null=True)
    reviewTitle = models.CharField(max_length=250, blank=True, null=True)
    reviewDescribe = models.CharField(max_length=250, blank=True, null=True)
    aboutTitle = models.CharField(max_length=250, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.aboutTitle
