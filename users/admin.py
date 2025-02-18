from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'first_name', 'last_name', 'role' , 'is_staff', 'is_superuser')
    search_fields = ('first_name', 'email')

admin.site.register(User, UserAdmin)