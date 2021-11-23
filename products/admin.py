from django.contrib import admin
from .models import (
    Product,
    UserProfile,
    UserRating,
    ProductSale,
    Category,
    UserReview,
    SMSMessage,
)

admin.site.site_header = "OneClick Admin"
admin.site.site_title = "OneClick Admin Portal"
admin.site.index_title = "Welcome to OneClick Admin Portal"


admin.site.site_header = "OneClick Admin"

# Register your models here.
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(UserRating)
admin.site.register(ProductSale)
admin.site.register(Category)
admin.site.register(UserReview)
admin.site.register(SMSMessage)
