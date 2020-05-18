from rest_framework import serializers
from rest_framework.authtoken.models import Token

from uptime import models


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bot
        fields = ('id', 'name')


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Server
        fields = ('id', 'hostname', 'protocol', 'date_added', 'date_changed', 'is_active')
