from django.http import request
from pusher import Pusher
from django.views.decorators.csrf import csrf_exempt
from rmp.decorators import add_cors_react_dev
from django.views.decorators.http import require_POST


# Create your views here.
@csrf_exempt
@add_cors_react_dev
@require_POST
def pusher_webhook(request: request):
    webhook = Pusher.validate_webhook(
        key=request.headers.get('X-Pusher-Key'),
        signature=request.headers.get('X-Pusher-Signature'),
        body=request.data
    )

    print(webhook)

    return 'ok'
