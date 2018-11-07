from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UsersListView(generics.ListAPIView):
    """
    GET users/
    Provides an endpoint to get a list of all the users registered in the application.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET users/:username/
    PUT users/:username/
    DELETE users/:username/
    Provides an endpoint to obtain details of a single user, update it or delete it from the application.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            user = self.queryset.get(username=kwargs['username'])
            return Response(UserSerializer(user).data)
        except User.DoesNotExist:
            return Response(
                data={
                    'message': 'User with username: {} does not exist'.format(kwargs['username'])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, *args, **kwargs):
        try:
            user = self.queryset.get(username=kwargs["username"])
            serializer = UserSerializer()
            updated_user = serializer.update(user, request.data)
            return Response(UserSerializer(updated_user).data)
        except User.DoesNotExist:
            return Response(
                data={
                    'message': 'User with username: {} does not exist'.format(kwargs['username'])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            user = self.queryset.get(username=kwargs['username'])
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(
                data={
                    'message': 'User with username: {} does not exist'.format(kwargs['username'])
                },
                status=status.HTTP_404_NOT_FOUND
            )
