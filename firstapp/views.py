from datetime import datetime
import random
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Messege, User, Chat
from .serializers import AllMessegesSerializer, LoginUsesSerializer, AllChatsSerializer
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404


class AllMessegeViewSet(APIView):
    def get(self, request):
        after = (request.GET['after'])
        id = (request.GET['chat_id'])
        user_name = (request.GET['user_name'])
        chat = Chat.objects.get(chat_id=id, user_name=user_name)

        if after != '0':
            current_time = datetime.strptime(after, '%Y-%m-%dT%H:%M:%S.%f')
            queryset = chat.chat_messages.filter(time_messege__gt=current_time).all()
        else:
            queryset = chat.chat_messages.all()

        serializer_class = AllMessegesSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        data = request.data
        chat_sender = Chat.objects.get(chat_id=data['chat_id'], user_name=data['sender_name'])
        if chat_sender:
            chat_receiver = Chat.objects.get(chat_id=data['chat_id'], user_name=data['name'])
            new_message_sender = Messege.objects.create(name=data['name'],
                                                        message=data['message'],
                                                        time_messege=timezone.now(),
                                                        message_chat = chat_sender)

            new_message_receiver = Messege.objects.create(name=data['name'],
                                                          message=data['message'],
                                                          time_messege=timezone.now(),
                                                          message_chat = chat_receiver)
            new_message_sender.save()
            new_message_receiver.save()

            serializer_class = AllMessegesSerializer(new_message_sender)
            return Response(serializer_class.data)
        return HttpResponseNotFound('<h1>Wrong chat id</h1>')


class AllUserViewSet(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer_class = LoginUsesSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        data = request.data
        user_login = get_object_or_404(User, login=data['name'], password=data['pass'])
        if user_login:
            user_login.online = True
            user_login.save()
            queryset = user_login.chats.all()
            serializer_class = AllChatsSerializer(queryset, many=True)
            return Response(serializer_class.data)


def uniq_chat_id(id):
    if Chat.objects.filter(chat_id=id).exists():
        return False
    else:
        return True


class AllChatViewSet(APIView):
    def get(self, request):
        queryset = Chat.objects.all()
        serializer_class = AllChatsSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        data = request.data
        user_login = get_object_or_404(User, login=data['name'])
        if user_login:
            id = random.randint(100, 500)
            uniq = uniq_chat_id(id)
            while not uniq:
                id = random.randint(100, 500)
                uniq = uniq_chat_id(id)

            new_chat_main = Chat.objects.create(user_name = data['name'],
                                           chat_id = id,
                                           users=User.objects.get(login=data['login'])
                                          )
            new_chat = Chat.objects.create(user_name = data['login'],
                                           chat_id = id,
                                           users=user_login
                                          )
            new_chat_main.save()
            new_chat.save()

            return JsonResponse({'create': True})
        return HttpResponseNotFound('<p>Not user</p>')
