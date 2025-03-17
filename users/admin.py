from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
    list_display= ('id', 'email', 'first_name', 'last_name', "phone_number",'role', "is_superuser")
    search_fields=('phone_number', 'email')

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)