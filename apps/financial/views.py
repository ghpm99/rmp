import json
import math
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from rmp.decorators import add_cors_react_dev, validate_user
from rmp.utils import boolean, format_date

from financial.models import Payment
from financial.utils import calculate_installments


@add_cors_react_dev
@validate_user
@require_GET
def get_all_view(request, user):

    req = request.GET
    filters = {}

    if req.get('status'):
        filters['status'] = req.get('status')
    if req.get('type'):
        filters['type'] = req.get('type')
    if req.get('name__icontains'):
        filters['name__icontains'] = req.get('name__icontains')
    if req.get('date__gte'):
        filters['date__gte'] = format_date(
            req.get('date__gte')) or datetime(2018, 1, 1)
    if req.get('date__lte'):
        filters['date__lte'] = format_date(
            req.get('date__lte')) or datetime.now() + timedelta(days=1)
    if req.get('installments'):
        filters['installments'] = req.get('installments')
    if req.get('payment_date__gte'):
        filters['payment_date__gte'] = format_date(
            req.get('payment_date__gte')) or datetime(2018, 1, 1)
    if req.get('payment_date__lte'):
        filters['payment_date__lte'] = format_date(
            req.get('payment_date__lte')) or datetime.now() + timedelta(days=1)
    if req.get('fixed'):
        filters['fixed'] = boolean(req.get('fixed'))
    if req.get('active'):
        filters['active'] = boolean(req.get('active'))

    datas = Payment.objects.filter(**filters).order_by('payment_date')

    payments = [{
        'id': data.id,
        'status': data.status,
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

    value_installments = calculate_installments(
        data.get('value'), installments)

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


@add_cors_react_dev
@validate_user
@require_GET
def detail_view(request, id, user):

    data = Payment.objects.filter(id=id).first()

    if(data is None):
        return JsonResponse({'msg': 'Payment not found'}, status=404)

    payment = {
        'id': data.id,
        'status': data.status,
        'type': data.type,
        'name': data.name,
        'date': data.date,
        'installments': data.installments,
        'payment_date': data.payment_date,
        'fixed': data.fixed,
        'active': data.active,
        'value': data.value
    }

    return JsonResponse({'data': payment})


@csrf_exempt
@add_cors_react_dev
@validate_user
@require_POST
def save_detail_view(request, id, user):

    data = json.loads(request.body)
    payment = Payment.objects.filter(id=id).first()

    if(data is None):
        return JsonResponse({'msg': 'Payment not found'}, status=404)

    if data.get('type'):
        payment.type = data.get('type')
    if data.get('name'):
        payment.name = data.get('name')
    if data.get('payment_date'):
        payment.payment_date = data.get('payment_date')
    if data.get('fixed'):
        payment.fixed = data.get('fixed')
    if data.get('active'):
        payment.active = data.get('active')
    if data.get('value'):
        payment.value = data.get('value')

    payment.save()

    return JsonResponse({'msg': 'ok'})


@csrf_exempt
@add_cors_react_dev
@validate_user
@require_POST
def payoff_detail_view(request, id, user):

    payment = Payment.objects.filter(id=id).first()

    if payment.status == 1:
        return JsonResponse({'msg': 'Pagamento ja baixado'}, status=400)

    date_format = '%Y-%m-%d'

    if payment.fixed is True:
        future_payment = payment.payment_date + relativedelta(months=1)
        payment_date = future_payment.strftime(date_format)
        new_payment = Payment(
            type=payment.type,
            name=payment.name,
            date=payment.date,
            installments=payment.installments,
            payment_date=payment_date,
            fixed=payment.fixed,
            value=payment.value
        )
        new_payment.save()

    payment.status = Payment.STATUS_DONE

    payment.save()

    return JsonResponse({'msg': 'Pagamento baixado'})


@add_cors_react_dev
@validate_user
@require_GET
def report_payment_view(request, user):

    query_fixed_debit = """
        SELECT
            SUM(value) as fixed_debit_total
        FROM
            financial_payment AS fixed_debit
        WHERE type=1 AND status=0 AND active=true AND fixed=true;
    """

    with connection.cursor() as cursor:
        cursor.execute(query_fixed_debit)
        fixed_debit = cursor.fetchone()

    query_fixed_credit = """
        SELECT
            SUM(value) as fixed_credit_total
        FROM
            financial_payment AS fixed_credit
        WHERE type=0 AND status=0 AND active=true AND fixed=true;
    """

    with connection.cursor() as cursor:
        cursor.execute(query_fixed_credit)
        fixed_credit = cursor.fetchone()

    queryOpen = """
        WITH debit AS (
            SELECT
                SUM(value) as debit_total,
                date_part('year', debit.payment_date) as debit_year,
                date_part('month', debit.payment_date) as debit_month
            FROM
                financial_payment AS debit
            WHERE type=1 AND status=0 AND active=true AND fixed=false
            GROUP BY
                date_part('year', debit.payment_date),
                date_part('month', debit.payment_date)
            ORDER BY
                date_part('year', debit.payment_date),
                date_part('month', debit.payment_date)
        ),
        credit AS (
            SELECT
                SUM(value) as credit_total,
                date_part('year', credit.payment_date) as credit_year,
                date_part('month', credit.payment_date) as credit_month
            FROM
                financial_payment AS credit
            WHERE type=0 AND status=0 AND active=true AND fixed=false
            GROUP BY
                date_part('year', credit.payment_date),
                date_part('month', credit.payment_date)
            ORDER BY
                date_part('year', credit.payment_date),
                date_part('month', credit.payment_date)
        )
        SELECT
            date_part('month', payment.payment_date) AS payment_month,
            date_part('year', payment.payment_date) AS payment_year,
            debit.debit_total as debit_total,
            credit.credit_total as credit_total
        FROM
            financial_payment AS payment
        LEFT JOIN
            debit
            ON
                debit.debit_year = date_part('year', payment.payment_date)
            AND
                debit.debit_month = date_part('month', payment.payment_date)
        LEFT JOIN
            credit
            ON
                credit.credit_year = date_part('year', payment.payment_date)
            AND
                credit.credit_month = date_part('month', payment.payment_date)
        WHERE status=0 AND active=true
        GROUP BY
            date_part('year', payment.payment_date),
            date_part('month', payment.payment_date),
            debit_total,
            credit_total
        ORDER BY payment_year, payment_month;
        """

    with connection.cursor() as cursor:
        cursor.execute(queryOpen)
        datas_open = cursor.fetchall()

    open = [{
        'label': str(math.trunc(data[0])) + '/' + str(math.trunc(data[1])),
        'debit': data[2],
        'credit': data[3]
    } for data in datas_open]

    query_closed = """
        WITH debit AS (
            SELECT
                SUM(value) as debit_total,
                date_part('year', debit.payment_date) as debit_year,
                date_part('month', debit.payment_date) as debit_month
            FROM
                financial_payment AS debit
            WHERE type=1 AND status=1 AND active=true
            GROUP BY
                date_part('year', debit.payment_date),
                date_part('month', debit.payment_date)
            ORDER BY
                date_part('year', debit.payment_date),
                date_part('month', debit.payment_date)
        ),
        credit AS (
            SELECT
                SUM(value) as credit_total,
                date_part('year', credit.payment_date) as credit_year,
                date_part('month', credit.payment_date) as credit_month
            FROM
                financial_payment AS credit
            WHERE type=0 AND status=1 AND active=true
            GROUP BY
                date_part('year', credit.payment_date),
                date_part('month', credit.payment_date)
            ORDER BY
                date_part('year', credit.payment_date),
                date_part('month', credit.payment_date)
        )
        SELECT
            date_part('month', payment.payment_date) AS payment_month,
            date_part('year', payment.payment_date) AS payment_year,
            debit.debit_total as debit_total,
            credit.credit_total as credit_total
        FROM
            financial_payment AS payment
        LEFT JOIN
            debit
            ON
                debit.debit_year = date_part('year', payment.payment_date)
            AND
                debit.debit_month = date_part('month', payment.payment_date)
        LEFT JOIN
            credit
            ON
                credit.credit_year = date_part('year', payment.payment_date)
            AND
                credit.credit_month = date_part('month', payment.payment_date)
        WHERE status=1 AND active=true
        GROUP BY
            date_part('year', payment.payment_date),
            date_part('month', payment.payment_date),
            debit_total,
            credit_total
        ORDER BY payment_year, payment_month;
        """

    with connection.cursor() as cursor:
        cursor.execute(query_closed)
        datas_closed = cursor.fetchall()

    closed = [{
        'label': str(math.trunc(data[0])) + '/' + str(math.trunc(data[1])),
        'debit': data[2],
        'credit': data[3]
    } for data in datas_closed]

    return JsonResponse({
        'data': {
            'open': open,
            'closed': closed,
            'fixed_debit': fixed_debit,
            'fixed_credit': fixed_credit
        }
    })
