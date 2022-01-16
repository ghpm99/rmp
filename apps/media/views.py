from django.shortcuts import render
import os
from media.models import Media


# Create your views here.
def index(request):
    context = {
        'media': 'N/A',
        'media_list': Media.objects.all(),
        'media_files': ''
    }
    return render(request, 'pages/media.html', context=context)
