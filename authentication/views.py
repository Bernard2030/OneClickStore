from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.mpesa_credentials import LipanaMpesaPpassword, MpesaAccessToken
from .serializers import ChangePasswordSerializer, MyTokenObtainPairSerializer, RegisterSerializer, UpdateUserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status


# sendgrid imports
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings


message = Mail(
    from_email='opiyodoro@gmail.com',
    to_emails='brobernard.254@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)

except Exception as e:
    print(e) 
     

# sending of sms messages
import africastalking


username = "YOUR_USERNAME"
api_key = "YOUR_API_KEY" 

africastalking.initialize(username, api_key)


# initialize SMS service
sms = africastalking.SMS


# response = sms.send("Hello world", ["+254791176810"])
# print(response)







# Create your views here.

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permissions_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permissions_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permissions_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class LogoutView(APIView):
    permissions_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



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