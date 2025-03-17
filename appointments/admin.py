from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient','doctor', 'date', 'time', 'status', 'created_at', 'updated_at', 'reason')
    search_fields = ('patient', 'doctor')

admin.site.register(Appointment)