from django.db import models
from ckeditor.fields import RichTextField

class FullView(models.Model):
    name = models.CharField(max_length=130, blank=True, null=True)
    img = models.ImageField(upload_to='img/', blank=True, null=True)
    img2 = models.ImageField(upload_to='img/', blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    url = models.CharField(max_length=350, blank=True, null=True)

    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Full'
        verbose_name_plural = 'Full View'



