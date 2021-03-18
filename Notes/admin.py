from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.site_header = 'Notes Dashboard'
admin.site.site_title = 'Notes Management'
admin.site.index_title = 'Notes Management Administration'

# Register your models here.


class Note_Admin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description',
                    'date', 'tags', 'favourites')
    list_filter = ('user', 'date', 'tags')
    search_fields = ['user', 'tags']


admin.site.register(Note, Note_Admin)
