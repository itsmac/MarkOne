# from rest_framework_simplejwt.serializers import TokenObtainSerializer
# from typing_extensions import Required
from django.contrib.auth import models
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import validators
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
# from rest_framework.utils import serializer_helpers


class RegisterSerializer(serializers.ModelSerializer):
    '''
    This is used to create a new user.
    '''
    email = serializers.EmailField(required = True,validators = [UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only = True, required = True, validators = [validate_password] )
    confirm_password = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = User
        fields = ('username','password','confirm_password','email','first_name','last_name')
        extra_kwargs = {
            'first_name' : {'required' : True},
            'last_name' : {'required' : True}
        }


    def validate(self, attrs):
        '''
        Validating the password and the password re enter fields are the same
        '''
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"Password": "Kindly check, Passwords did not match"})

        return attrs
    
    
    def create(self, validated_data):
        '''
        Creation of users happen after validating
        '''
        user = User.objects.create(
            email = validated_data['email'],
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

    
class UpdateProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')
        extra_kwargs = {
        'first_name' : {'required' : True},
        'last_name' : {'required' : True}
        }
        
   
    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk = user.pk).filter(email = value).exists():
            raise serializers.ValidationError({"email" : "This email is already taken"})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk = user.pk).filter(username = value).exists():
            raise serializers.ValidationError({"username": "Username already taken"})
        return value

    def update(self, instance, validated_data):

        if User.pk != instance.pk: raise serializers.ValidationError({"Auth Error": "User Not authenticated."})

        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.user_name = validated_data['username']

        instance.save()

        return instance






