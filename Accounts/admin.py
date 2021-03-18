from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.


class Profile_Admin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'phone', 'email')
    list_filter = ('user', 'nickname', 'phone')
    search_fields = ['user', 'phone']


admin.site.register(Profile, Profile_Admin)
