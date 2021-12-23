from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CreateUserSerializer, UserListSerializer, DeleteUserSerializer


User = get_user_model()


class CreateUserView(CreateAPIView):
    """
    API endpoint for creating of users
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class DeleteUserView(APIView):
    """
    API endpoint for deletion of users
    """
    serializer_class = DeleteUserSerializer
    
    def post(self, request):
        deleted_user = DeleteUserSerializer(data=request.data)
        username = request.data['username']
        
        if deleted_user.is_valid(raise_exception=True):    
            User.objects.get(username=username).delete()
           
            return Response({"user {}".format(username): "deleted"})
        else:
            return Response({"user {}".format(username): "error during deletion"})


class UserListView(ListAPIView):
    """
    API endpoint for display a list of registered users (with pagination)
    """
    queryset = User.objects.all().order_by('first_name')
    permission_classes = (IsAuthenticated,) #You can comment that get access to users list without authorization
    serializer_class = UserListSerializer
    paginator_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'department']