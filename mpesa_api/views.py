from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getAccessToken(request):
    return HttpResponse("<h1>Get Access Token</h1>")
