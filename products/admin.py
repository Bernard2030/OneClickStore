from django.contrib import admin
from .models import Product, UserProfile, UserRating

# Register your models here.
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(UserRating)

