from django.shortcuts import render

# Create your views here.
# mpesa_api views

from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import LipanaMpesaPpassword, MpesaAccessToken

# Create your views here.
def getAccessToken(request):
    consumer_key = '0iAFjJP6WV434Q27FAJLHzCZxXdNXZhf'
    consumer_secret = 'IssZ6odZILd9EOyh'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validate_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validate_mpesa_access_token)
    


def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token 
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": "254791176810",
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": "254791176810",
        "CallBackURL":"https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Bernard",
        "TransactionDesc": "Testing stk push"

    }   
    response = requests.post(api_url, json = request, headers=headers)
    return HttpResponse('success')