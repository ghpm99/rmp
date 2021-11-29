from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'text': 'routines'
    }
    return render(request, 'pages/routines.html', context=context)

def kanban(request):

    return render(request, 'pages/kanban.html')

def financial(request):

    return render(request, 'pages/financial.html')
