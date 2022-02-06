from django.views.decorators.csrf import csrf_exempt
from rmp.decorators import add_cors_react_dev
from django.views.decorators.http import require_POST
from lib import pusher


# Create your views here.
@csrf_exempt
@add_cors_react_dev
@require_POST
def pusher_webhook(request):
    return pusher.webhook(request)
