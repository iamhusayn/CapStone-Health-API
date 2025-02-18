from django.contrib import admin
from .models import Doctor

# Register your models here.
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'speciality', 'is_staff', 'is_superuser')
    search_fields = ('user', 'bio')

admin.site.register(Doctor)