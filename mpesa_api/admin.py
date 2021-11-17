from django.contrib import admin
from .models import MpesaPayments

# Register your models here.
admin.site.register(MpesaPayments)

admin.site.site_header = "OneClick Admin"
