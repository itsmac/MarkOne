# from typing_extensions import Required
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from .managers import CustomUserAccountManager

# Create your models here.

# class Roles(models.Model):
#     role_name = models.CharField(max_length = 100, blank=True,null=True)

#     def __str__(self) -> str:
#         return self.role_name


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    SELLER = 2
    CUSTOMER = 3
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (SELLER, 'Seller'),
        (CUSTOMER, 'Customer')
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    # is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.PositiveSmallIntegerField( ROLE_CHOICES ,blank = True, null= True, default = 3 )
    phone_no = models.CharField(max_length=10)
    start_date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = CustomUserAccountManager()

    def __str__(self) -> str:
        return self.email





# class User(AbstractUser):
#     roles = models.ManyToManyField(Roles)