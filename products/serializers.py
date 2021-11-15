from rest_framework import serializers

from .models import Product, UserProfile, UserRating, User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'date_added')
        read_only_fields = ('id', 'date_added')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'profile_pic', 'location', 'date_joined')
        read_only_fields = ('id', 'user')


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model
    """
    product = ProductSerializer(many=True, read_only=True)
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'product', 'profile')
        read_only_fields = ('id', 'username', 'email')


class RatingSerializer(serializers.ModelSerializer):
    """
    Serializer for UserRating model
    """

    class Meta:
        model = UserRating
        fields = ('id', 'user', 'rating')
        read_only_fields = ('id', 'user', 'rating')
