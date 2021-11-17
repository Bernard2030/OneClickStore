from django.contrib import admin
from .models import Product, UserProfile, UserRating, ProductSale, Category


admin.site.site_header = "OneClick Admin"

# Register your models here.
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(UserRating)
admin.site.register(ProductSale)
admin.site.register(Category)


