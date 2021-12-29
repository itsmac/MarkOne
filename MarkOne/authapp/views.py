from django.db.models import query
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, serializers
from .serializers import RegisterSerializer, UpdateProfileSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
class RegisterView(generics.CreateAPIView):
    permission_class = (AllowAny,)
    query_set = User.objects.all()
    serializer_class = RegisterSerializer

class UpdateProfileView(generics.UpdateAPIView):
    permission_class = (IsAuthenticated)
    queryset = User.objects.all()
    serializer_class = UpdateProfileSerializer
