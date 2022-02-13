import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from lib import pusher
from remote.models import Config
from rmp.decorators import add_cors_react_dev, validate_user
from django.views.decorators.http import require_POST, require_GET


# Create your views here.
@csrf_exempt
@add_cors_react_dev
@require_POST
@validate_user
def send_command_view(request, user):
    pusher.send_command(json.loads(request.body).get('cmd'))
    return JsonResponse({'msg': 'ok'})


@add_cors_react_dev
@require_GET
@validate_user
def screen_size_view(request, user):
    screen_size = get_object_or_404(Config, type=Config.CONFIG_SCREEN)
    print(screen_size.value)
    return JsonResponse(screen_size.value)
