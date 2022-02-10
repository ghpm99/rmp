from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rmp.decorators import add_cors_react_dev
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
import json


@csrf_exempt
@add_cors_react_dev
@require_POST
def login_view(request):
    data = json.loads(request.body)
    print(data)
    if 'credentials' in data:
        user = authenticate(
            username=data['credentials']['username'],
            password=data['credentials']['password']
        )
        if(user is not None):
            print(user)
            login(request, user)
            return JsonResponse({
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_staff': user.is_staff
            })
        else:
            return JsonResponse({'msg': 'user not found'}, status=404)

    return JsonResponse({'msg': 'credentials is missing'}, status=400)
