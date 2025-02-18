from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from .models import User
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

@csrf_exempt
@api_view(['POST'])
class RegisterView(APIView):
    permission_classes = [AllowAny] 
      
    def RegisterView(request):
        user = User.objects.create_user(
            username=data['email'],
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            role=data['role']
        )

        if request.method == 'GET':
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data, safe= False)
        
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = UserSerializer(data, data=request.data)

            if serializer.is_valid():
                user = serializer.save()
                return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)