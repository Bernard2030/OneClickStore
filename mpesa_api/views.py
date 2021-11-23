# mpesa_api views

from django.http import HttpResponse, JsonResponse
import requests
from requests.api import options
from requests.auth import HTTPBasicAuth
import json
from .mpesa_credentials import LipanaMpesaPpassword, MpesaAccessToken
from django.views.decorators.csrf import csrf_exempt
from .models import MpesaPayments


# Create your views here.
def getAccessToken(request):
    consumer_key = 'CG4A9WH3V9EpKlB2jUGmvnblHdebKlhD'
    consumer_secret = 'SnhOwSKglXbCmLou'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validate_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validate_mpesa_access_token)


def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": "254791176810",
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": "254705814086",
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Bernard",
        "TransactionDesc": "Testing stk push"

    }
    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse('success')


@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://6095-154-159-238-95.ngrok.io/api/v1/c2b/confirmation",
               "ValidationURL": "https://6095-154-159-238-95.ngrok.io/api/v1/c2b/validation"
               }
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)


@csrf_exempt
def call_back(request):
    pass


@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    mpesa_body = request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)

    payment = MpesaPayments(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        amount=mpesa_payment['TransAmount'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],
    )
    payment.save()

    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))
