from rest_framework import serializers
from .models import Messege, User, Chat


class AllMessegesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messege
        fields = ['name', 'message', 'time_messege', 'get_time']


class AllChatsSerializer(serializers.ModelSerializer):
    chat_messages = AllMessegesSerializer(many=True)

    class Meta:
        model = Chat
        fields = ['user_name', 'chat_id', 'get_online', 'chat_messages', ]


class LoginUsersSerializer(serializers.ModelSerializer):
    chats = AllChatsSerializer(many=True)

    class Meta:
        model = User
        fields = ['login', 'password', 'online', 'chats']


class AllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login']
