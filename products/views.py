from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DeleteView, ListView
from rest_framework import viewsets
from .serializers import ProductSerializer, UserProfileSerializer, UserSerializer, RatingSerializer
from .models import Product, UserProfile, UserRating


def index(request):
    return render(request, 'products/index.html')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-date_added')
    serializer_class = ProductSerializer


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    ordering = ['-date_added']
    paginate_by = 10


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
