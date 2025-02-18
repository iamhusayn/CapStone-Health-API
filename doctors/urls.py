from django.urls import path, include
from .views import UserViewSet, DoctorViewSet
from rest_framework.routers import DefaultRouter
from .views import CustomAuthToken
from .views import DoctorListView, DoctorCreateView


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('api/doctors/search/', DoctorViewSet.as_view({'get': 'list'}), name='doctor-search'),
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/create/', DoctorCreateView.as_view(), name='doctor-create'),
]
