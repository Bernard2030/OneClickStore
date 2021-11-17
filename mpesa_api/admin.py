from django.contrib import admin
from mpesa_api.models import MpesaPayments

# Register your models here.
admin.site.register(MpesaPayments)

admin.site.site_header = "OneClick Admin"
