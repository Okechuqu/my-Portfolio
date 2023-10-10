from django.db import models
from webapp.models.completed_project import FullView
from ckeditor.fields import RichTextField



class ProjectCategory(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    category = models.CharField(
        max_length=150, help_text='Must to be seperated by a "-"')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'project selector'
        verbose_name_plural = 'project selectors'


class Project(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    category_name = models.ForeignKey(
        "webapp.ProjectCategory", on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/', blank=True, null=True)
  
    shortDescribe = models.TextField(
        max_length=50, blank=True, null=True, help_text='Max-letters is 50')
    view_modal = models.ForeignKey(
        FullView, blank=True, null=True,  on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
