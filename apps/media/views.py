from django.http import JsonResponse, request
from django.shortcuts import render
from django.views.decorators.http import require_GET
from media.models import Media
from rmp.decorators import add_cors_react_dev
from rmp.utils import paginate


# Create your views here.
def index(request):
    context = {
        'media': 'N/A',
        'media_list': Media.objects.all(),
        'media_files': ''
    }
    return render(request, 'pages/media.html', context=context)


@add_cors_react_dev
@require_GET
def get_media_files(request: request) -> JsonResponse:
    media_list = Media.objects.all()

    medias = [{
        'id': media.id,
        'order': media.order,
        'name': media.name,
    } for media in media_list]
    data = paginate(medias, (request.GET.get('page') or None))
    return JsonResponse(data)


@add_cors_react_dev
@require_GET
def get_media_playing(request: request) -> JsonResponse:
    media_playing = Media.objects.filter(status=Media.S_PLAYING)

    if(media_playing.exists()):

        media = {
            'id': media_playing[0].id,
            'name': media_playing[0].name
        }
    else:
        media = {
            'id': 0,
            'name': 'N/a'
        }
    return JsonResponse(media)
