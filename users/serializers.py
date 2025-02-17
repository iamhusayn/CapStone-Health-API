from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'role',]
        extra_kwargs = {'tokens': {'read_only': True}}

    def get_tokens(self, obj):
        refresh = RefreshToken.for_user(obj)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            }

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            return super().update(instance, validated_data)
        

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    tokens = serializers.SerializerMethodField()
    
    def get_tokens(self, obj):
        user = authenticate(email=obj['email'], password=obj['password'])
        if user:
            return user.tokens()
        raise serializers.ValidationError('Invalid credentials')
    
    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        return {'email': user.email, 'tokens': user.tokens()}