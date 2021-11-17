from cloudinary import uploader
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DeleteView, ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductSerializer, UserProfileSerializer, UserSerializer, RatingSerializer, ReviewSerializer, \
    ProductSaleSerializer, CategorySerializer
from .models import Product, UserProfile, UserRating, UserReview, ProductSale, Category
import os
from dotenv import load_dotenv

load_dotenv()


def index(request):
    return render(request, 'products/index.html')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-date_added')
    for query in Product.objects.all():
        queryset.image = os.environ.get('CLOUDINARY_ROOT') + str(query.image)
    # print(queryset.image)
    serializer_class = ProductSerializer


class NewProductView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    def get(self, request):
        products = Product.objects.all().order_by('-date_added')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        image = request.data['image']
        upload_data = uploader.upload(image)
        serializer = ProductSerializer(data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save(image=upload_data['url'])
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    ordering = ['-date_added']
    paginate_by = 10


class ProductSearchView(ListAPIView):
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def get_queryset(self):
        queryset = Product.objects.all()
        product_search = self.request.query_params.get('name')
        category_search = self.request.query_params.get('category')
        if product_search:
            queryset = queryset.filter(name__icontains=product_search)
        return queryset

    def post(self, request, format=None):
        products = Product.objects.filter(name__icontains=request.data['name'])
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class CategorySearchView(ListAPIView):
    serializer_class = CategorySerializer

    filterset_fields = ['name']

    def get_queryset(self):
        queryset = Category.objects.all()
        category_search = self.request.query_params.get('name')
        if category_search:
            queryset = queryset.filter(name__icontains=category_search)
        return queryset


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.owner:
            return True
        return False


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = UserRating.objects.all()
    serializer_class = RatingSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = UserReview.objects.all()
    serializer_class = ReviewSerializer


class ProductSaleViewSet(viewsets.ModelViewSet):
    queryset = ProductSale.objects.all()
    serializer_class = ProductSaleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
