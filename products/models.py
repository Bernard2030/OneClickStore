from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/products/{}".format(self.id)

    @classmethod
    def get_all_products(cls):
        return cls.objects.all()

    @classmethod
    def get_product_by_id(cls, id):
        return cls.objects.get(id=id)

    @classmethod
    def get_products_image_url(cls):
        return cls.image.url


class UserProfile(models.Model):
    """
    User Profile model
    """
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, default="Nairobi, KE")
    date_joined = models.DateField(auto_now_add=True, blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True default='profile_pics/default.jpg')
    profile_pic = CloudinaryField('image',
                                  default="https://res.cloudinary.com/dd5ab8mp3/image/upload/v1634660213/image/upload/v1/images/profile/user.jpg")
    contact_email = models.EmailField(max_length=100, blank=True)
    contact_phone = models.CharField(max_length=11, blank=True)
    products = models.ManyToManyField(Product, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    def __str__(self):
        return f'{self.user.username}: profile'

    def get_absolute_url(self):
        return "/profile/{}".format(self.id)

    @classmethod
    def get_all_users(cls):
        return cls.objects.all()

    @classmethod
    def get_user_by_id(cls, id):
        return cls.objects.get(id=id)

    @classmethod
    def get_user_image_url(cls):
        return cls.profile_pic.url

    def get_username(self):
        return self.user.username

    def get_email(self):
        return self.user.email

    def get_location(self):
        return self.location

    def get_date_joined(self):
        return self.date_joined

    def get_contact_email(self):
        return self.contact_email

    def get_contact_phone(self):
        return self.contact_phone

    def get_user(self):
        return self.user

    def get_user_id(self):
        return self.user.id

    def get_products(self):
        return self.products

    def get_product_count(self):
        return self.products.count()

    def get_total_user_count(self):
        return UserProfile.objects.count()


class UserRating(models.Model):
    """
    Project Rating model
    """
    rating = ()
    for x in enumerate(range(1, 6)):
        rating_tuple = (x[1], f'{x[1]}')
        rating += (rating_tuple,)

    # print(rating)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_ratings", null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    rating = models.FloatField(choices=rating, default=0, blank=True)
    total_rating = models.FloatField(default=0, blank=True)

    def __str__(self):
        return f'{self.user}: rating'

    def get_absolute_url(self):
        return "/profile/{}".format(self.id)

    def get_user(self):
        return self.user

    def get_user_id(self):
        return self.user.id

    def get_rating(self):
        return self.rating

    def get_date(self):
        return self.date


class UserReview(models.Model):
    """
    Project Review model
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="user_reviews", null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    review = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.user.username}: review'

    def get_absolute_url(self):
        return "/profile/{}".format(self.id)

    def get_user(self):
        return self.user

    def get_user_id(self):
        return self.user.id

    def get_review(self):
        return self.review

    def get_date(self):
        return self.date


class ProductSale(models.Model):
    """
    Product Sale model
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_sales", null=True)
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="buyer_sales", null=True)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="seller_sales", null=True)
    date_sold = models.DateTimeField(auto_now_add=True, blank=True)
    quantity = models.IntegerField(default=0, blank=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)

    def __str__(self):
        return f'{self.product.name}: sale'

    def get_absolute_url(self):
        return "/products/{}".format(self.id)

    def get_product(self):
        return self.product

    def get_product_id(self):
        return self.product.id

    def get_date(self):
        return self.date_sold

    def get_quantity(self):
        return self.quantity

    def get_total_price(self):
        return self.sale_price


class SMSMessage(models.Model):
    """
    SMS Message model
    """
    number = models.CharField(max_length=13, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="sms_messages", null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.user.username}: message'

    def get_absolute_url(self):
        return "/message/{}".format(self.id)

    def get_user(self):
        return self.user

    def get_user_id(self):
        return self.user.id

    def get_message(self):
        return self.message

    def get_date(self):
        return self.date
