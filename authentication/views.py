from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    ChangePasswordSerializer,
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    UpdateUserSerializer,
)
from products.serializers import SMSMessageSerializer, EmailMessageSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.social_serializers import TwitterLoginSerializer
import africastalking
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from products.models import SMSMessage, EmailMessage

load_dotenv()


def send_email(email, subject, message):
    # send email
    try:
        message = Mail(
            from_email=os.environ.get("EMAIL_HOST_USER"),
            to_emails=email,
            subject=subject,
            html_content=message,
        )
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return True
    except Exception as e:
        print(e.body)
        return False, e.body


class SendEmailMessageView(APIView):
    # permission_classes = (IsAuthenticated,)
    parser_classes = [JSONParser]
    serializer_class = EmailMessageSerializer

    def post(self, request):
        email = request.data["email"]
        subject = request.data["subject"]
        message = request.data["message"]
        print(send_email(email, subject, message))
        if send_email(email, subject, message) == True:
            try:
                EmailMessage.objects.create(
                    email=email, subject=subject, message=message
                )
                print(
                    Response(
                        {"message": "Email saved successfully"},
                        status=status.HTTP_200_OK,
                    )
                )
            except Exception as e:
                print(e)
                return Response(
                    {"message": "Email not sent", "error": e},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response({"message": "Email sent"}, status=status.HTTP_200_OK)
        return Response(
            {"success": False, "errors": str(send_email(email, subject, message)[1])},
            status=status.HTTP_400_BAD_REQUEST,
        )


at_username = os.environ.get("AT_USERNAME")
at_api_key = os.environ.get("AT_API_KEY")

africastalking.initialize(at_username, at_api_key)

# initialize SMS service
sms = africastalking.SMS
app = africastalking.Application


# sending of sms messages
def send_sms(phone_number, message):
    # send SMS
    try:
        # print(phone_number)
        print(app.fetch_application_data())
        user_message = sms.send(message, [phone_number])
        if user_message:
            try:
                SMSMessage.objects.create(
                    number=phone_number,
                    message=message,
                )
                return "message saved"
            except Exception as e:
                print(e)
            return True
    except Exception as e:
        print(e)
        return False


class SendMessageView(APIView):
    # permission_classes = (IsAuthenticated,)
    parser_classes = [JSONParser]
    serializer_class = SMSMessageSerializer

    def post(self, request):
        """
        Send a message to a user
        ---
        ## Send Message route
        type:
            number:
                type: string
                required: true
            message:
                type: string
                required: true
        parameters:
            - number: number
              message: message
        responseMessages:
            - code: 200
              message: Message sent successfully
            - code: 400
              message: Message not sent
        """
        phone_number = request.data["phone_number"]
        message = request.data["message"]
        if send_sms(phone_number, message):
            return Response({"success": True}, status=status.HTTP_200_OK)
        return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)


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
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter
