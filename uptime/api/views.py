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


class BotViewSet(viewsets.ModelViewSet):
    queryset = models.Bot.objects.all()
    serializer_class = api_serializers.BotSerializer
    permission_classes = [IsAuthenticated]


class ServerViewSet(viewsets.ModelViewSet):
    serializer_class = api_serializers.ServerReadSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        #return models.Server.objects.filter(user=self.request.user)
        return models.Server.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'create' or self.action == 'put':
            return api_serializers.ServerWriteSerializer
        return self.serializer_class


class EndpointViewSet(viewsets.ModelViewSet):
    serializer_class = api_serializers.EndpointSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Endpoint.objects.filter(server__id=self.kwargs['server_pk'])


class ServerProtocolViewSet(viewsets.ModelViewSet):
    queryset = models.ServerProtocol.objects.all()
    serializer_class = api_serializers.ServerProtocolSerializer
    permission_classes = [IsAuthenticated]