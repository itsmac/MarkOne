from django.contrib.auth.models import BaseUserManager, PermissionsMixin

class CustomUserAccountManager(BaseUserManager, PermissionsMixin):
    def create_user():
        