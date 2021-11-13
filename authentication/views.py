from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import ChangePasswordSerializer, MyTokenObtainPairSerializer, RegisterSerializer, UpdateUserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status


<<<<<<< HEAD
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







=======
>>>>>>> 69a888a078d0ea022ce04b1eef6354ac27c2f909
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
