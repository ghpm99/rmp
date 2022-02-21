from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from rmp.decorators import add_cors_react_dev, validate_user
from django.views.decorators.csrf import csrf_exempt
import json
from financial.models import Payment


@add_cors_react_dev
@validate_user
@require_GET
def get_all_view(request, user):
    datas = Payment.objects.filter(active=True)

    payments = [{
        'type': data.type,
        'name': data.name,
        'date': data.date,
        'installments': data.installments,
        'payment_date': data.payment_date,
        'fixed': data.fixed
    } for data in datas]
    return JsonResponse({'data': payments})


@csrf_exempt
@add_cors_react_dev
@validate_user
@require_POST
def save_new_view(request, user):
    data = json.loads(request.body)
    payment = Payment(
        type=data.get('type'),
        name=data.get('name'),
        date=data.get('date'),
        installments=data.get('installments'),
        payment_date=data.get('payment_date'),
        fixed=data.get('fixed')
    )
    payment.save()
    return JsonResponse({'msg': 'Pagamento incluso com sucesso'})
