from django.db.models import query
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, serializers
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UpdateProfileSerializer, UpdatePasswordSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class RegisterView(generics.CreateAPIView):
    permission_class = (AllowAny,)
    query_set = User.objects.all()
    serializer_class = RegisterSerializer

class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_class = (IsAuthenticated,)
    serializer_class = UpdateProfileSerializer

class UpdatePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_class = (IsAuthenticated,)
    serializer_class = UpdatePasswordSerializer


class LogoutUserView(APIView):
    permission_class = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)