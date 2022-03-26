import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from lib import pusher
from remote.models import Config, Screenshot
from rmp.decorators import add_cors_react_dev, validate_user
from django.views.decorators.http import require_POST, require_GET
from django.core.files import File
from django.conf import settings
import os


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
    data = json.loads(screen_size.value)
    return JsonResponse(data)


@csrf_exempt
@add_cors_react_dev
@require_POST
@validate_user
def hotkey_view(request, user):
    data = json.loads(request.body)
    hotkey = data.get('hotkey')
    pusher.send_hotkey(hotkey)
    return JsonResponse({'msg': 'Ok'})


@csrf_exempt
@add_cors_react_dev
@require_POST
@validate_user
def key_press_view(request, user):
    data = json.loads(request.body)
    keys = data.get('keys')
    pusher.send_key_press(keys)
    return JsonResponse({'msg': 'Ok'})


@csrf_exempt
@add_cors_react_dev
@require_POST
@validate_user
def mouse_move_view(request, user):
    data = json.loads(request.body)
    x = data.get('x')
    y = data.get('y')
    pusher.mouse_move(x, y)
    return JsonResponse({'msg': 'Ok'})


@csrf_exempt
@add_cors_react_dev
@require_POST
@validate_user
def mouse_button_view(request, user):
    data = json.loads(request.body)
    button = data.get('button')
    pusher.mouse_button(button)
    return JsonResponse({'msg': 'Ok'})


@csrf_exempt
@add_cors_react_dev
@require_POST
@validate_user
def save_screenshot_view(request, user):
    req_files = request.FILES
    if not req_files.get('image'):
        return JsonResponse({'msg': 'Nao existe nenhuma imagem anexo'}, status=400)

    fullname = os.path.join(settings.MEDIA_ROOT, 'screenshot/screenshot.png')
    print(fullname)
    if os.path.exists(fullname):
        os.remove(fullname)

    file = request.FILES.get('image').file

    screenshot = Screenshot.objects.filter(id=1).first()

    if screenshot is None:
        screenshot = Screenshot()

    screenshot.image.save('screenshot.png', File(file), save=True)

    pusher.notify_screenshot()

    return JsonResponse({'msg': 'Ok'})


@csrf_exempt
@add_cors_react_dev
@require_POST
@validate_user
def mouse_scroll_view(request, user):
    data = json.loads(request.body)
    value = data.get('value')
    pusher.mouse_scroll(value)
    return JsonResponse({'msg': 'Ok'})


def mouse_move_and_button(request, user):
    data = json.loads(request.body)
    x = data.get('x')
    y = data.get('y')
    button = data.get('button')
    pusher.mouse_move_button(x, y, button)
    return JsonResponse({'msg': 'Ok'})
