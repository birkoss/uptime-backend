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


class ServerViewSet(viewsets.ModelViewSet):
    queryset = models.Server.objects.all()
    serializer_class = api_serializers.ServerSerializer
