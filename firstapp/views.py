from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Сategory
from .serializers import СategorySerializer, AllСategoriesSerializer, CardSerializer


def index(request):
    return HttpResponse("<p>1. <a href=all_categories>Список категорий</a></p>"
                        "<p>2. <a href=all_objects>Список всех карточек товаров категории</a></p>"
                        "<p>3. <a href=all_cards>Детальная информация о карточках</a></p>"
                        "<p>4. Для перехода на определенную карточку пропишите в адресной строке "
                        "<code style='font-size: 15px;'><b>/card/pk</b></code>  (где <code>pk</code> номер нужной карточка)"
                        "<h4>Пример: <code style='font-size: 15px;'><a href='/card/2'>http://127.0.0.1:8000/card/2</a></code></h4></p>")


class AllObjectViewSet(APIView):
    def get(self, request):
        queryset = Сategory.objects.filter(parent=None).prefetch_related("children").all()
        serializer_class = СategorySerializer(queryset, many=True)
        return Response(serializer_class.data)


class AllСategoriesViewSet(APIView):
    def get(self, request):
        queryset = Сategory.objects.filter(parent=None).prefetch_related("children").all()
        serializer_class = AllСategoriesSerializer(queryset, many=True)
        return Response(serializer_class.data)


class AllСardsViewSet(APIView):
    def get(self, request):
        queryset = Сategory.objects.filter(level=4).all()
        serializer_class = CardSerializer(queryset, many=True)
        return Response(serializer_class.data)


class OneСardsViewSet(APIView):
    def get(self, request, pk):
        queryset = Сategory.objects.filter(level=4).all()[pk-1]
        serializer_class = CardSerializer([queryset], many=True)
        return Response(serializer_class.data)
