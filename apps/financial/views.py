from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from financial.utils import calculate_installments
from rmp.decorators import add_cors_react_dev, validate_user
from django.views.decorators.csrf import csrf_exempt
import json
from financial.models import Payment
from datetime import datetime
from dateutil.relativedelta import relativedelta


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
        'fixed': data.fixed,
        'value': data.value
    } for data in datas]
    return JsonResponse({'data': payments})


@csrf_exempt
@add_cors_react_dev
@validate_user
@require_POST
def save_new_view(request, user):

    data = json.loads(request.body)

    installments = data.get('installments')
    payment_date = data.get('payment_date')

    value_installments = calculate_installments(data.get('value'), installments)

    date_format = '%Y-%m-%d'

    for i in range(installments):
        payment = Payment(
            type=data.get('type'),
            name=data.get('name'),
            date=data.get('date'),
            installments=i + 1,
            payment_date=payment_date,
            fixed=data.get('fixed'),
            value=value_installments[i]
        )
        payment.save()
        date_obj = datetime.strptime(payment_date, date_format)
        future_payment = date_obj + relativedelta(months=1)
        payment_date = future_payment.strftime(date_format)

    return JsonResponse({'msg': 'Pagamento incluso com sucesso'})
