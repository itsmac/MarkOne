from django.urls import path,include
from .views import RegisterView,UpdateProfileView

urlpatterns = [
    path('register/',RegisterView.as_view(), name = 'register'),
    path('updateprofile/<int:pk>/', UpdateProfileView.as_view(), name = 'updateprofile' ),
]