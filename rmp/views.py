from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'text': 'index'
    }
    return render(request, 'pages/index.html', context=context)


def login(request):

    return render(request, 'pages/login.html')
