from django.db import models
from ckeditor.fields import RichTextField



class myServices(models.Model):
    service = models.CharField(max_length=150, blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.service
    
    class Meta:
        verbose_name = 'my service'
        verbose_name_plural = 'My services'



class Service(models.Model):
    icon = models.CharField(max_length=150, blank=True, null=True)
    title = models.ForeignKey('webapp.myServices', on_delete=models.CASCADE,related_name='my_services')

    def __str__(self):
        return self.icon
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'services'


