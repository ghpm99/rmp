from django.shortcuts import render
from .forms import SendVideoForm

from web.models import Youtube


# Create your views here.
def index(request):
    context = {
        'text': 'web'
    }
    return render(request, 'pages/web.html', context=context)


def youtube(request):
    if(request.method == 'POST'):
        form = SendVideoForm(request.POST)
        if(form.is_valid()):

            print(form)
    else:
        form = SendVideoForm()

    context = {
        'video_list': Youtube.objects.all(),
        'form': form
    }
    print(context)
    return render(request, 'pages/youtube.html', context=context)


def navigation(request):

    return render(request, 'pages/navigation.html')
