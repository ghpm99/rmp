from django.shortcuts import render

from rmp.settings import PUSHER_CLIENT


# Create your views here.
def index(request):
    PUSHER_CLIENT.trigger('rmp', 'mediafilesrequest', {})
    context = {
        'text': 'testes2'
    }
    return render(request, 'pages/media.html', context=context)
