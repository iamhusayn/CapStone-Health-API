from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class User(AbstractUser, PermissionsMixin):
        
        ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
     )
         
        username = True
        first_name= models.CharField(max_length=250)
        last_name= models.CharField(max_length=250)
        email = models.EmailField(unique=True)
        phone_number= models.CharField(max_length=11, null=True, unique=True, blank=True)
        role = models.CharField(max_length=10, choices=ROLE_CHOICES, blank=False, null=False, default='')

        
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []

        objects = CustomUserManager()
    
        def __str__(self):
         return f"{self.username} - {self.role}"
        
        
        
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models
# from .managers import UserManager
# from rest_framework_simplejwt.tokens import RefreshToken



# # Create your models here.
# class User(AbstractBaseUser, PermissionsMixin): #PermissionsMixin
#     ROLE_CHOICES = (
#         ('patient', 'Patient'),
#         ('doctor', 'Doctor'),
#     )
#     email = models.EmailField(max_length=255, unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
    
#     objects = UserManager()
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'role']
    
#     def __str__(self):
#         return self.first_name
    
#     def tokens(self):
#         refresh = RefreshToken.for_user(self)
#         return {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }