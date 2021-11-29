from django.http import JsonResponse


def socket(request):
    if(request.method == 'GET'):
        return JsonResponse({'message': 'Hello World!'})