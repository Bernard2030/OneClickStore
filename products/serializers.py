
from rest_framework import serializers
from cloudinary.models import CloudinaryField
from .models import Product, ProductSale, UserProfile, UserRating, User, UserReview, Category


class ProductSerializer(serializers.ModelSerializer):
    image = CloudinaryField('image')
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category', 'date_added')
        read_only_fields = ('id', 'date_added')


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        read_only_fields = ('id', 'username', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for UserProfile model
    """
    product = ProductSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'profile_pic', 'location', 'product', 'date_joined')
        read_only_fields = ('id', 'user', 'date_joined'),


class RatingSerializer(serializers.ModelSerializer):
    """
    Serializer for UserRating model
    """

    class Meta:
        model = UserRating
        fields = ('id', 'user', 'rating')
        read_only_fields = ('id', 'user', 'rating')


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for UserReview model
    """

    class Meta:
        model = UserReview
        fields = ('id', 'user', 'review')
        read_only_fields = ('id', 'user', 'review')


class ProductSaleSerializer(serializers.ModelSerializer):
    """
    Serializer for ProductSale model
    """
    product = ProductSerializer( read_only=True)

    class Meta:
        model = ProductSale
        fields = ('id', 'product', 'sale_price', 'date_sold')
        read_only_fields = ('id', 'product', 'sale_price', 'date_sold')


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model
    """
    product = ProductSerializer( read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'product')
        read_only_fields = ('id', 'name', 'product')
