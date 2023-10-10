from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Languages(models.Model):
    language = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    ability = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'language'
        verbose_name_plural = 'languages'



class Intro(models.Model):
    logo = models.ImageField(upload_to='media/logo', blank=True, null=True)
    bgimg = models.ImageField(upload_to='media/', blank=True, null=True)
    img = models.ImageField(upload_to='media/', blank=True, null=True)
    intro = RichTextField(blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    about = RichTextField(blank=True, null=True)
    language = models.ManyToManyField('webapp.Languages', related_name='portfolioLanguage' )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Intro'
        verbose_name_plural = 'Introduction'


class SiteInfo(models.Model):
    favicon = models.ImageField(upload_to='img/favicon', blank=True, null=True)
    statsBgImg = models.ImageField(upload_to='img', blank=True, null=True)
    siteName = models.CharField(max_length=250, blank=True, null=True)
    pageTitle = models.CharField(max_length=250, blank=True, null=True)
    pageSEO = RichTextField(blank=True, null=True)
    contactUsNote = models.CharField(max_length=220, blank=True, null=True)

    phone = models.IntegerField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.siteName

    class Meta:
        verbose_name = 'site'
        verbose_name_plural = 'site Info'