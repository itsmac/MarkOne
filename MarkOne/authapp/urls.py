from django.urls import path,include
import rest_framework
from .views import LogoutUserView, RegisterView,UpdateProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/',RegisterView.as_view(), name = 'register'),
    path('login/', TokenObtainPairView.as_view(), name = 'token_obtain'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('login/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('updateprofile/<int:pk>/', UpdateProfileView.as_view(), name = 'updateprofile' ),
]