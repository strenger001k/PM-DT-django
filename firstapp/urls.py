from django.urls import path
from .views import *


urlpatterns = [
    path('messeges', AllMessegeViewSet.as_view()),
    path('login', AllUserViewSet.as_view()),
    path('chat', AllChatViewSet.as_view()),
]
