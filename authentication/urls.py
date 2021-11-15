from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from authentication.views import MyObtainTokenPairView, RegisterView, ChangePasswordView, UpdateProfileView, LogoutView
# mpesa_api
from authentication import views

urlpatterns = [

    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('update_profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # mpesa_api

    path('access/token/',views.getAccessToken,name='get_mpesa_access_token'),

    
    
]
