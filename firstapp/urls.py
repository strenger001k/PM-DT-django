from django.urls import path
from .views import *


urlpatterns = [
    path('users', AllUserViewSet.as_view()),
]
