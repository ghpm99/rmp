from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'text': 'web'
    }
    return render(request, 'pages/web.html', context=context)

def youtube(request):

    return render(request, 'pages/youtube.html')

def navigation(request):

    return render(request, 'pages/navigation.html')
