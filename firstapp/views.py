from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import AllUsersSerializer


class AllUserViewSet(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer_class = AllUsersSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        new_user = User.objects.create(name=data['name'], message=data['message'])
        new_user.save()
        serializer_class = AllUsersSerializer(new_user)
        return Response(serializer_class.data)
