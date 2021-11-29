from django.shortcuts import render
import os
from media.models import Media
from rmp.local_settings import CAMINHO_MEDIAS


# Create your views here.
def index(request):
    context = {
        'media': 'N/A',
        'media_list': Media.objects.all(),
        'media_files': os.listdir(CAMINHO_MEDIAS)
    }
    return render(request, 'pages/media.html', context=context)
