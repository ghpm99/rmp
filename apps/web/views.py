from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from rmp.decorators import add_cors_react_dev
from django.shortcuts import render

from .forms import SendVideoForm

from web.models import Youtube


# Create your views here.
def index(request):
    context = {
        'text': 'web'
    }
    return render(request, 'pages/web.html', context=context)


def youtube(request):
    if(request.method == 'POST'):
        form = SendVideoForm(request.POST)
        if(form.is_valid()):

            print(form)
    else:
        form = SendVideoForm()

    context = {
        'video_list': Youtube.objects.all(),
        'form': form
    }
    print(context)
    return render(request, 'pages/youtube.html', context=context)


def navigation(request):

    return render(request, 'pages/navigation.html')


@csrf_exempt
@add_cors_react_dev
@require_POST
def change_screen(request) -> JsonResponse:
    return JsonResponse({'msg': 'ok'})
