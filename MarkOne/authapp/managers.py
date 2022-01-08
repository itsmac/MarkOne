from django.contrib.auth.models import BaseUserManager, PermissionsMixin

class CustomUserAccountManager(BaseUserManager):
    def create_superuser(self,email,password, **other_fields):
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('role',1)

        return self.create_user(email,password, **other_fields)


    def create_user(self,email,password, **other_fields):
        if not email:
            raise ValueError("Email should be filled")
        if not password:
            raise ValueError("Password should be filled")
        
        user = self.model(email = email, **other_fields)
        user.set_password(password)
        user.save()
        return user
    

        