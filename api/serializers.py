from rest_framework import serializers
from rest_framework.authtoken.models import Token

from uptime import models

from user.models import User


# Serializer for the Authenticated User (including the API token)
class AuthUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'is_active', 'is_staff', 'token')
        read_only_fields = ('id', 'is_active', 'is_staff')
    
    def get_token(self, obj):
        token = Token.objects.get(user=obj)
        return token.key


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bot
        fields = ('id', 'name')


class EmptySerializer(serializers.Serializer):
    pass


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Server
        fields = ('id', 'hostname', 'protocol', 'date_added', 'date_changed', 'is_active')


# Serializer for the User Login
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(required=True, write_only=True)