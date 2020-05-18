from rest_framework import serializers
from rest_framework.authtoken.models import Token

from uptime import models


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bot
        fields = ('id', 'name')


class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Endpoint
        fields = ('id', 'url', 'date_added')


class ServerSerializer(serializers.ModelSerializer):
    endpoints = EndpointSerializer(many=False, read_only=True)

    class Meta:
        model = models.Server
        fields = ('id', 'hostname', 'protocol', 'date_added', 'date_changed', 'is_active', 'endpoints')
