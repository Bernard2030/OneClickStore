from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

from . import views

schema_view = get_swagger_view(title='Online Store API')
router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'userprofiles', views.UserProfileViewSet)
router.register(r'ratings', views.RatingViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'product-sales', views.ProductSaleViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'reviews', views.ReviewViewSet)
# router.register(r'search-products', views.ProductSearchView)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/new-product/', views.NewProductView.as_view(), name='new-product'),
    path('api/products-search/', views.ProductSearchView.as_view(), name='product-search'),
    path('api/category-search', views.CategorySearchView.as_view(), name='category-search'),
    path('api-docs/', schema_view, name="api-docs"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/products-all/', views.ProductListView.as_view(), name='product-list'),
    # path('logout/', views.LogoutView.as_view(), {"next_page": '/'}),
    path('api-token-auth/', obtain_auth_token),
    # path('<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    # path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

]


