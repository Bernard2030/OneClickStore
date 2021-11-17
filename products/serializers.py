from rest_framework import serializers
from cloudinary.models import CloudinaryField
from .models import Product, ProductSale, UserProfile, UserRating, User, UserReview, Category
import os
from dotenv import load_dotenv

load_dotenv()


class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    category_name = serializers.StringRelatedField(source='category.name')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['image'] = self.get_image_url(instance)
        return ret

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image','category', 'date_added', 'category_name')
        read_only_fields = ('id', 'date_added')

    def get_image_url(self, obj):
        return os.environ.get('CLOUDINARY_ROOT') + str(obj.image)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance


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

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['profile_pic'] = self.get_user_image_url(instance)
        return ret

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'profile_pic', 'location', 'product', 'date_joined')
        read_only_fields = ('id', 'user', 'date_joined'),

    def get_user_image_url(self, obj):
        return str(obj.profile_pic)


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
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductSale
        fields = ('id', 'product', 'sale_price', 'date_sold')
        read_only_fields = ('id', 'product', 'sale_price', 'date_sold')


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model
    """
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'product')
        read_only_fields = ('id', 'product')
