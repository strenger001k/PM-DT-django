from django.contrib import admin
from firstapp.models import User
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

@admin.register(User)
class StateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'message',)
