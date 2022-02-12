import os
from django.http import JsonResponse
import pusher

pusher_client = pusher.Pusher(
    app_id=os.environ.get('ENV_PUSHER_APP_ID'),
    key=os.environ.get('ENV_PUSHER_KEY'),
    secret=os.environ.get('ENV_PUSHER_SECRET'),
    cluster=os.environ.get('ENV_PUSHER_CLUSTER'),
    ssl=True
)


def send_command(command):
    pusher_client.trigger('private-display', 'command', {'cmd': command})


def webhook(request):
    webhook = pusher_client.validate_webhook(
        key=request.headers.get('X-Pusher-Key'),
        signature=request.headers.get('X-Pusher-Signature'),
        body=request.body
    )

    if(webhook is None):
        print('Webhook incorreto')
        return JsonResponse({'msg': 'Webhook incorreto'}, status=400)

    for event in webhook['events']:
        if event['name'] == "channel_occupied":
            if(event["channel"] == 'private-status'):
                pusher_client.trigger('private-events', 'status-channel', {'occupied': True})
            print("Channel occupied: %s" % event["channel"])
        elif event['name'] == "channel_vacated":
            if(event["channel"] == 'private-status'):
                pusher_client.trigger('private-events', 'status-channel', {'occupied': False})
            print("Channel vacated: %s" % event["channel"])

    return JsonResponse({'msg': 'ok'})


def auth(request, channel_name, socket_id):
    auth_response = pusher_client.authenticate(channel=channel_name, socket_id=socket_id)
    return JsonResponse(auth_response)
