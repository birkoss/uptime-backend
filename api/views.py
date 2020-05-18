from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404

from rest_framework import serializers, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from uptime import models

from . import serializers as api_serializers


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = api_serializers.EmptySerializer
    
    @action(methods=['POST',], detail=False)
    def login(self, request):
        serializer = api_serializers.UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        print(serializer.validated_data.get('email'))
        print(serializer.validated_data.get('password'))
        user = authenticate(email=serializer.validated_data.get('email'), password=serializer.validated_data.get('password'))
        if user is None:
            raise serializers.ValidationError("Invalid username/password. Please try again!")

        data = api_serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)


class BotViewSet(viewsets.ModelViewSet):
    queryset = models.Bot.objects.all()
    serializer_class = api_serializers.BotSerializer


class ServerViewSet(viewsets.ModelViewSet):
    queryset = models.Server.objects.all()
    serializer_class = api_serializers.ServerSerializer


# class ServerViewSet2(viewsets.ViewSet):
#     def list(self, request):
#         queryset = models.Server.objects.all()
#         serializer = ServerSerializer
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         queryset = models.Server.objects.all()
#         server = get_object_or_404(queryset, pk=pk)
#         serializer = ServerSerializer(server)
#         return Response(serializer.data)


class userLogin(APIView):
    def post(self, request, format=None):
        user = authenticate(request,  email=request.data['email'],  password=request.data['password'])
        if user is not None:
            login(request, user)

            token = Token.objects.get(user=user)

            return Response({
                'status': status.HTTP_200_OK,
                'item': request.data,
                'token': token.key,
            })
        else:
            return Response({
                "status": status.HTTP_401_UNAUTHORIZED,
                "title": "Unauthorized",
                "message": "The request has not been applied because it lacks valid authentication credentials for the target resource."
            })


class userRegister(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.create_user(
                serializer.data['email'],
                request.data['password']
            )

            token = Token.objects.get(user=user)

            return Response({
                'status': status.HTTP_200_OK,
                'item': serializer.data,
                'token': token.key,
            })
        else:
            return ResponseApiSerializerError(serializer)