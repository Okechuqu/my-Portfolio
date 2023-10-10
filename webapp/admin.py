from django.contrib import admin
from .models import *

# Register your models here.


class TitleAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Title.objects.exists():
            return False
        return True
    
class SiteAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if SiteInfo.objects.exists():
            return False
        return True

class IntroAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Intro.objects.exists():
            return False
        return True

admin.site.register(Intro, IntroAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(ClientReview)
admin.site.register(myServices)
admin.site.register(Statistics)
admin.site.register(FullView)
admin.site.register(Languages)
admin.site.register(SiteInfo, SiteAdmin)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(ProjectCategory)
