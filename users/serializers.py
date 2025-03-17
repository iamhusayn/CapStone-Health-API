from rest_framework import serializers, viewsets, status
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
           user = User.objects.create_user(**validated_data)
  
           return user



User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'email', 'password', 'role']

    def validate(self, data):
        request = self.context.get('request')
        
        # Prevent non-superusers from registering as superuser
        if request and not request.user.is_superuser and 'is_superuser' in data:
            raise serializers.ValidationError("You do not have permission to create a superuser.")

        return data

    def create(self, validated_data):
        role = validated_data.pop('role')
        user = User.objects.create_user(**validated_data, role=role)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        role = data.get("role")

        user = authenticate(username=username, password=password)
        
        if user is None:
            raise serializers.ValidationError("Invalid username or password.")

        if user.role != role:
            raise serializers.ValidationError(f"Invalid role. You are registered as a {user.role}.")

        data["user"] = user
        return data





    # email = serializers.EmailField()
    # password = serializers.CharField(write_only=True)
    # tokens = serializers.SerializerMethodField()
    
    # def get_tokens(self, obj):
    #     user = authenticate(email=obj['email'], password=obj['password'])
    #     if user:
    #         return user.tokens()
    #     raise serializers.ValidationError('Invalid credentials')
    
    # def validate(self, data):
    #     user = authenticate(email=data['email'], password=data['password'])
    #     if not user:
    #         raise serializers.ValidationError('Invalid credentials')
    #     return {'email': user.email, 'tokens': user.tokens()}