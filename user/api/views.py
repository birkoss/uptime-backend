from django.contrib.auth import authenticate, login, logout
from rest_framework import serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ..models import User

from . import serializers as user_serializers


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['POST'], detail=False)
    def login(self, request):
        serializer = user_serializers.UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data.get('email'), password=serializer.validated_data.get('password'))
        if user is None:
            raise serializers.ValidationError("Invalid username/password. Please try again!")

        data = user_serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def register(self, request):
        serializer = user_serializers.UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(email=serializer.validated_data.get('email'), password=serializer.validated_data.get('password'))
        data = user_serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated])
    def change_password(self, request):
        serializer = user_serializers.UserPasswordChangeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        request.user.set_password(serializer.validated_data.get('new_password'))
        request.user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
