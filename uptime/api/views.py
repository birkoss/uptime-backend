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
from . import helpers as api_helpers


class BotViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only ViewSet for Bot
    """
    queryset = models.Bot.objects.all()
    serializer_class = api_serializers.BotSerializer
    permission_classes = [IsAuthenticated]


class ServerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Server
    """
    serializer_class = api_serializers.ServerReadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Server.objects.filter(
            api_helpers.apiGetUserFilters(user=self.request.user)
        )

    def perform_create(self, serializer):
        args = {}
        if not self.request.user.is_staff:
            args = {'user': self.request.user}

        serializer.save(
            **args
        )

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'put':
            if self.request.user.is_staff:
                return api_serializers.ServerWriteStaffSerializer
            else:
                return api_serializers.ServerWriteUserSerializer
        return self.serializer_class

    def handle_exception(self, exc):
        return Response({
            "error": exc.__str__()
        })


class EndpointViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Endpoint
    """
    serializer_class = api_serializers.EndpointSerializer
    permission_classes = [IsAuthenticated]

    def initial(self, request, *args, **kwargs):
        """
        Validate that the parent Server is owned by the User
        """
        get_object_or_404(
            models.Server.objects.filter(
                api_helpers.apiGetUserFilters(user=self.request.user)
            ), pk=kwargs['server_pk']
        )

        viewsets.ModelViewSet.initial(self, request, *args, **kwargs)

    def get_queryset(self):
        """
        Validate that the Endpoint is from the parent Server
        """
        return models.Endpoint.objects.filter(
            server__id=self.kwargs['server_pk']
        )

    def perform_create(self, serializer):
        """
        Apply the parent Server
        """
        serializer.save(
            server=get_object_or_404(
                models.Server.objects.filter(
                    api_helpers.apiGetUserFilters(user=self.request.user)
                ), pk=self.kwargs['server_pk']
            )
        )


class ServerProtocolViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only ViewSet for ServerProtocol
    """
    queryset = models.ServerProtocol.objects.all()
    serializer_class = api_serializers.ServerProtocolSerializer
    permission_classes = [IsAuthenticated]


class PingViewSet(viewsets.ModelViewSet):
    serializer_class = api_serializers.PingReadSerializer
    permission_classes = [IsAuthenticated]

    def initial(self, request, *args, **kwargs):
        """
        Validate that the parent Server and Endpoint is owned by the User
        """
        server = get_object_or_404(
            models.Server.objects.filter(
                api_helpers.apiGetUserFilters(user=self.request.user)
            ), pk=kwargs['server_pk']
        )

        endpoint = get_object_or_404(
            models.Endpoint.objects.filter(
                server=server
            ), pk=kwargs['server_endpoint_pk']
        )

        viewsets.ModelViewSet.initial(self, request, *args, **kwargs)

    def get_queryset(self):
        """
        Validate that the Pink is from the parent Server and Endpoint
        """
        return models.Ping.objects.filter(
            endpoint__server__id=self.kwargs['server_pk'],
            endpoint__id=self.kwargs['server_endpoint_pk']
        )

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'put':
            return api_serializers.PingWriteSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """
        Apply the parent Endpoint
        """
        serializer.save(
            endpoint=get_object_or_404(
                models.Endpoint.objects.all(),
                pk=self.kwargs['server_endpoint_pk']
            )
        )
