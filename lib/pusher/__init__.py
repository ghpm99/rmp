import os
import pusher

PUSHER_CLIENT = pusher.Pusher(
    app_id=os.environ.get('ENV_PUSHER_APP_ID'),
    key=os.environ.get('ENV_PUSHER_KEY'),
    secret=os.environ.get('ENV_PUSHER_SECRET'),
    cluster=os.environ.get('ENV_PUSHER_CLUSTER'),
    ssl=True
)


def send_command(command):
    PUSHER_CLIENT.trigger('krill', 'command', {'cmd': command})
