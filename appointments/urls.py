from django.urls import path
from .views import AppointmentCreateView, AppointmentListView, AppointmentUpdateView

urlpatterns = [
    path('appointments/list', AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointments/<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment-update'),
]
