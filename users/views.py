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
# class UserCreateView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = 


@api_view(['POST'])
@csrf_exempt
def RegisterView(request):
    # data = request.data(user)
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


        # return Response({"message": "User registered successfully"})

# @api_view(['POST'])
# class RegisterView(APIView):
#     permission_classes = [AllowAny]
    
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        # data = request.data
        # email = data.get('email', None)
        # password = data.get('password', None)
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # if email is None or password is None:
        #     return Response({ "error": "Please provide both email and password" }, status=status.HTTP_400_BAD_REQUEST)
        
        # user = authenticate(email=email, password=password)
        
        # if not user:
        #     return Response({ "error": "Invalid credentials" }, status=status.HTTP_404_NOT_FOUND)
        
        # access = AccessToken.for_user(user)
        # return Response({ "token": str(access) }, status=status.HTTP_200_OK)
    
