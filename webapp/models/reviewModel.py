from django.db import models
from ckeditor.fields import RichTextField


class ClientReview(models.Model):
    client_img = models.ImageField(upload_to='cl-img/', blank=True, null=True)
    client_name = models.CharField(max_length=150, blank=True, null=True)
    client_job = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    feedback = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'Reviews'

