from django.contrib.auth import get_user_model, password_validation
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from ..models import User
from ..managers import UserManager


class AuthUserSerializer(serializers.ModelSerializer):
    """
    A user serializer for the authenticated User (and returning the token)
    """
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'is_active', 'is_staff', 'token')
        read_only_fields = ('id', 'is_active', 'is_staff')
    
    def get_token(self, obj):
        token = Token.objects.get(user=obj)
        return token.key


class EmptySerializer(serializers.Serializer):
    """
    An empty serializer which accepts nothing
    """
    pass


class UserLoginSerializer(serializers.Serializer):
    """
    A user serializer for logging in the user
    """
    email = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'password')

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError('Email is already taken')
        
        return UserManager.normalize_email(value)
    
    def validate_password(self, value):
        password_validation.validate_password(value)
        return value
