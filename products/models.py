from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/products/{}".format(self.id)
