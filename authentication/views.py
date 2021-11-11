from django.shortcuts import render
from rest_framework import permissions
from rest_framework.permissions import  AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer,RegisterSerializer
from rest_framework import generics

# Create your views here.

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permissions_classes = (AllowAny,)
    serializer_class = RegisterSerializer    
