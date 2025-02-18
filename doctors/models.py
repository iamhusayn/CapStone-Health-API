from django.db import models
from users.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractUser

# class UserDoc(AbstractUser):
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#     ]
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     age = models.PositiveIntegerField()

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialty = models.CharField(max_length=255)
    bio = models.TextField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name()