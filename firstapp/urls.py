from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('all_objects', AllObjectViewSet.as_view()),
    path('all_categories', AllСategoriesViewSet.as_view()),
    path('all_cards', AllСardsViewSet.as_view()),
    path('card/<int:pk>', OneСardsViewSet.as_view()),
]
