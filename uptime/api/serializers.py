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


class ServerProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServerProtocol
        fields = ('id', 'name', 'slug')


class ServerWriteStaffSerializer(serializers.ModelSerializer):
    protocol = ServerProtocolSerializer(many=False, read_only=True)
    protocol_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = models.Server
        fields = (
            'id',
            'hostname',
            'protocol',
            'protocol_id',
            'user_id',
            'is_active'
        )


class ServerWriteUserSerializer(serializers.ModelSerializer):
    protocol = ServerProtocolSerializer(many=False, read_only=True)
    protocol_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = models.Server
        fields = (
            'id',
            'hostname',
            'protocol',
            'protocol_id',
            'is_active'
        )


class ServerReadSerializer(serializers.ModelSerializer):
    protocol = ServerProtocolSerializer(many=False, read_only=True)

    class Meta:
        model = models.Server
        fields = (
            'id',
            'hostname',
            'protocol',
            'date_added',
            'date_changed',
            'is_active'
        )


class PingReadSerializer(serializers.ModelSerializer):
    bot = BotSerializer(many=False, read_only=True)
    endpoint = EndpointSerializer(many=False, read_only=True)

    class Meta:
        model = models.Ping
        fields = (
            'endpoint',
            'bot',
            'response_code',
            'response_time',
            'response_headers',
            'response_body'
        )


class PingWriteSerializer(serializers.ModelSerializer):
    bot = BotSerializer(many=False, read_only=True)
    bot_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = models.Ping
        fields = (
            'bot',
            'bot_id',
            'response_code',
            'response_time',
            'response_headers',
            'response_body'
        )
