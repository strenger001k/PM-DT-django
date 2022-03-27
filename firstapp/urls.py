from django.urls import path
from .views import *


urlpatterns = [
    path('messeges', AllMessegeViewSet.as_view()),  # методом ГЕТ возвращает все сообщения; методом ПОСТ отправляет
    path('login', AllUserViewSet.as_view()),  # метод ГЕТ возвращает ВСЮ инфу про каждого(в плоть до смс); метод ПОСТ для входа в акк и вывода все инфы про акк
    path('signup', SignUpViewSet.as_view()),  # метод ПОСТ просто регает
    path('chat', AllChatViewSet.as_view()),  # метод ГЕТ возвращает все чаты; метод ПОСТ создает новый чат
    path('logout', LogOutView.as_view()),  # метод ГЕТ выход из сети
    path('all_username', AllUsersnameViewSet.as_view()),  # метод ГЕТ получить всех зареганых пользователей
    path('', index)
]
