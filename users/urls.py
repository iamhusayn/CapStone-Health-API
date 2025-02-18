from django.urls import path, include
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView, name='register'),
    path('login/', LoginView, name='login'),
]