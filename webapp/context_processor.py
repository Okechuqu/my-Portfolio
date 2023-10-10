from webapp.models import *
from webapp.forms import *


def frontendContextProcessor(request):
    return {
        'statistics': Statistics.objects.all(),
        'reviews': ClientReview.objects.all(),
        'introAll': Intro.objects.all(),
        'introFirst': Intro.objects.all().first(),
        'sites': SiteInfo.objects.all().first(),
        'skillset': FullView.objects.all(),
        'services': Service.objects.all(),
        'projects': Project.objects.all(),
        'categories': ProjectCategory.objects.all(),
        'titles': Title.objects.all().first(),
        'form': ClientForm,
    }
