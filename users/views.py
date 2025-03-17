from .serializers import UserSerializer, LoginSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from django.contrib.auth import login
from rest_framework.authtoken.models import Token




# @api_view(['POST'])
class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            user = serializer.save()

            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "message": "Registration successful",
                "username": user.username,
                "email": user.email,
                "role": user.role,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    # parser_classes = [JSONParser]
    # permission_classes = [AllowAny]
    
    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         return Response({'message': 'User registered successfully!', 'user': UserSerializer(user).data}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login API
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data["user"]
            login(request, user)  # Log in the user
            token, created = Token.objects.get_or_create(user=user)  # Generate token for authentication

            return Response({
                "message": "Login successful",
                "token": token.key,
                "username": user.username,
                "email": user.email,
                "role": user.role
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)















    # parser_classes = [JSONParser]
    # permission_classes = [AllowAny]
    
    # def post(self, request):
    #     username = request.data.get('username')
    #     password = request.data.get('password')
    #     user = authenticate(username=username, password=password)
        
    #     if user == user:
    #         return Response({'message': f'Welcome {username}, you have logged in successfully!', 'user': UserSerializer(user).data}, status=status.HTTP_200_OK)
    #     return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


























# @api_view(http_method_names=['GET'])
# def list_users(self, request):
#     return Response(data=UserSerializer.data, status=status.HTTP_200_OK)



# class RegisterView(APIView):
#   permission_classes = [permissions.AllowAny]
 
#   def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response("user registration successfull. User created", status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

# class LoginView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#           data =request.data
#           email =data.get('email', None)
#           password = data.get('password', None)

#           if email is None or password is None:
#               return Response({'error':'please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
          
#           user = authenticate( username = email, password=password)

#           if not user:
#               return Response({'error': 'invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
          
          
#           access = AccessToken.for_user(user)
#           return Response({'token': str(access)}, status=status.HTTP_200_OK)


































# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework import generics, permissions
# from django.contrib.auth import get_user_model
# from rest_framework.response import Response
# from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework import status
# from rest_framework.permissions import AllowAny
# from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import AccessToken
# from .models import User
# from django.views.decorators.csrf import csrf_exempt

# User = get_user_model()

# @csrf_exempt
# @api_view(['POST'])
# class RegisterView(APIView):
#     permission_classes = [AllowAny] 
      
#     def RegisterView(request):
#         user = User.objects.create_user(
#             username=data['email'],
#             email=data['email'],
#             password=data['password'],
#             first_name=data['first_name'],
#             last_name=data['last_name'],
#             role=data['role']
#         )

#         if request.method == 'GET':
#             user = User.objects.all()
#             serializer = UserSerializer(user, many=True)
#             return Response(serializer.data, safe= False)
        
#         elif request.method == 'POST':
#             data = JSONParser().parse(request)
#             serializer = UserSerializer(data, data=request.data)

#             if serializer.is_valid():
#                 user = serializer.save()
#                 return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# class LoginView(APIView):
#     permission_classes = [AllowAny]
    
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)

#         if serializer.is_valid():
#             return Response(serializer.validated_data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)