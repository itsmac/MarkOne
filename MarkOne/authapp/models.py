from typing_extensions import Required
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Roles(models.Model):
    ADMIN = 1
    SELLER = 2
    CUSTOMER = 3
    ROLE_CHOICES = (
        (ADMIN,'admin'),
        (SELLER,'seller'),
        (CUSTOMER,'customer'),
    )
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key= True)

    def __str__(self) -> str:
        return self.get_id_display()


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    role = models.ForeignKey( Roles ,on_delete=CASCADE)
    phone_no = models.CharField(max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','password',]


    



# class User(AbstractUser):
#     roles = models.ManyToManyField(Roles)