from django.contrib import admin
from firstapp.models import Messege, Chat, User
from django.contrib import admin
from mptt.admin import MPTTModelAdmin


@admin.register(Messege)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'message_chat',)


@admin.register(Chat)
class StateAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'chat_id', 'users',)


@admin.register(User)
class StateAdmin(admin.ModelAdmin):
    list_display = ('login', 'password', 'online')
