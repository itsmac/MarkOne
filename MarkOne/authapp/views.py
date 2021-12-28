from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.
class RegisterView(generics.CreateAPIView):
    permission_class = (AllowAny,)
    query_set = User.objects.all()
    serializer_class = RegisterSerializer
