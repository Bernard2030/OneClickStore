from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from authentication.views import MyObtainTokenPairView, RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, \
    FacebookLogin, TwitterLogin
from dj_rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)


urlpatterns = [

    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('update_profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
<<<<<<< HEAD

  
    
    
=======
    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('dj-rest-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
    path(
        'socialaccounts/',
        SocialAccountListView.as_view(),
        name='social_account_list'
    ),
    path(
        'socialaccounts/<int:pk>/disconnect/',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    )
>>>>>>> 4590ca4db4282e5b9d613f3c58f7ccc037cb8fc9
]