import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from lib import pusher
from rmp.decorators import add_cors_react_dev, validate_user
from django.views.decorators.http import require_POST


# Create your views here.
@csrf_exempt
@add_cors_react_dev
@require_POST
@validate_user
def send_command_view(request, user):
    print(user)
    print(request)
    pusher.send_command(json.loads(request.body).get('cmd'))
    return JsonResponse({'msg': 'ok'})
