from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager






class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, first_name, last_name, password=None, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password) 
        user.save()
        return user

    def create_superuser(
        self, email, phone_number, first_name, last_name, password=None
    ):
        user = self.create_user(
            email=email,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=256, unique=True)
    first_name = models.CharField(max_length=256, null=False, blank=False)
    last_name = models.CharField(max_length=256, null=False, blank=False)
    user_name = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True) 
    is_superuser = models.BooleanField(default=False) 
    social_id = models.CharField(max_length=256, blank=True, null=True)
    provider = models.CharField(max_length=256, blank=True, null=True)
    
    
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number", "first_name", "last_name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser