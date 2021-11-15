from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    def get_profile_pic(self):
        return self.profile_pic.url

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

    @receiver(post_save)
    def update_total_score(sender, instance, created, **kwargs):
        if created:
            total_rating = UserRating.objects.filter(user=instance.user).aggregate(Sum('rating'))
            instance.total_rating = total_rating['rating__sum']/UserRating.objects.filter(user=instance.user).count()
            print(instance.total_rating)
            instance.total_rating = round(instance.total_rating, 2)
            instance.save()

    def __str__(self):
        return f'{self.user.username}: rating'

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

    def get_total_score(self):
        return self.total_score
