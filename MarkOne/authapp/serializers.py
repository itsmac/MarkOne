from django.core.exceptions import ValidationError
from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUserModel
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.contrib.auth import authenticate
# from rest_framework.utils import serializer_helpers



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True, write_only = True)
    confirm_password = serializers.CharField(required = True, write_only = True)
    access = serializers.CharField(read_only = True)
    refresh = serializers.CharField(read_only = True)
    role = serializers.CharField(read_only = True) 

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password does not match !"})

        email = attrs['email']
        password = attrs['password']
        user = authenticate(email, password)

        if user is None:
            raise serializers.ValidationError("Ivalid Credentials")
        
        try:
            refresh_token_object = RefreshToken.for_user(user)
            refresh_token = str(refresh_token_object)
            # access_token = AccessToken.for_user(user)
            access_token = refresh_token_object.access_token

            validated_userinfo = {
                'refresh_token' : refresh_token,
                'access_token' : access_token,
                'email' : user.email,
                'role' : user.role
                
            }

        except:
            return serializers.ValidationError("Invalid login")

        return validated_userinfo
        


class RegisterSerializer(serializers.ModelSerializer):
    '''
    This is used to create a new user.
    '''
    class Meta:
        model = CustomUserModel
        fields = '__all__'


    # def validate(self, attrs):
    #     '''
    #     Validating the password and the password re enter fields are the same
    #     '''
    #     if attrs['password'] != attrs['confirm_password']:
    #         raise serializers.ValidationError({"Password": "Kindly check, Passwords did not match"})

    #     return attrs
    
    def create(self, validated_data):

        auth_user = CustomUserModel.objects.create_user(**validated_data)   #(**validated_data)
        return auth_user
    
    
    # def create(self, validated_data):
    #     '''
    #     Creation of users happen after validating
    #     '''
    #     user = User.objects.create(
    #         email = validated_data['email'],
    #         username = validated_data['username'],
    #         first_name = validated_data['first_name'],
    #         last_name = validated_data['last_name']
    #     )

    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

    
class UpdateProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True)

    class Meta:
        model = CustomUserModel
        fields = '__all__'
        
   
    # def validate_email(self, value):
    #     user = self.context['request'].user
    #     if User.objects.exclude(pk = user.pk).filter(email = value).exists():
    #         raise serializers.ValidationError({"email" : "This email is already taken"})
    #     return value

    # def validate_username(self, value):
    #     user = self.context['request'].user
    #     if User.objects.exclude(pk = user.pk).filter(username = value).exists():
    #         raise serializers.ValidationError({"username": "Username already taken"})
    #     return value

    # def update(self, instance, validated_data):
    #     user = self.context['request'].user
    #     if user.pk != instance.pk: raise serializers.ValidationError({"Auth Error": "User Not authenticated."})

    #     instance.first_name = validated_data['first_name']
    #     instance.last_name = validated_data['last_name']
    #     instance.email = validated_data['email']
    #     instance.user_name = validated_data['username']

    #     instance.save()

    #     return instance
    

class UpdatePasswordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUserModel
        fields = ('password','confirm_password','oldpassword')
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password does not match !"})
        
    def validate_existing_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value) :
            raise serializers.ValidationError({"password":"Existing incorrect password"})
        return Response({"Success": True})
        # return super().validate(attrs)
        
    def update(self, instance, validated_data):
        user = self.context['request'].user
        
        if user.pk != instance.pk : raise serializers.ValidationError({"Auth Error": "User Not authenticated."})
        instance.set_password(validated_data['password'])
        instance.save()
        return Response({
            "Success": True,
            "data" : instance
            })
    





