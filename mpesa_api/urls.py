from django.urls import path
from . import views


urkpatterns = [
    path('access/token',views.getAccessToken,name='get_mpesa_access_token'),

]