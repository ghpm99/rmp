from django.http import JsonResponse, request
from django.shortcuts import render
from django.views.decorators.http import require_GET
from media.models import Media
from rmp.utils import paginate


# Create your views here.
def index(request):
    context = {
        'media': 'N/A',
        'media_list': Media.objects.all(),
        'media_files': ''
    }
    return render(request, 'pages/media.html', context=context)


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
