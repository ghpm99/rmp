import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from lib.pusher.pusher_lib import send_command
from rmp.decorators import add_cors_react_dev
from django.views.decorators.http import require_POST


# Create your views here.
@csrf_exempt
@add_cors_react_dev
@require_POST
def send_command_view(request):
    send_command(json.loads(request.body).get('cmd'))
    return JsonResponse({'msg': 'ok'})
