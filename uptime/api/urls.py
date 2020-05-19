from rest_framework_nested import routers
from django.urls import include, path

from . import views as api_views

router = routers.SimpleRouter()

router.register(r'servers', api_views.ServerViewSet, basename='server')

servers_router = routers.NestedSimpleRouter(router, r'servers', lookup='server')
servers_router.register(r'endpoints', api_views.EndpointViewSet, basename='server_endpoint')

endpoints_router = routers.NestedSimpleRouter(servers_router, r'endpoints', lookup='server_endpoint')
endpoints_router.register(r'pings', api_views.PingViewSet, basename='server_endpoint_ping')

router.register(r'bots', api_views.BotViewSet, basename='bot')
router.register(r'protocols', api_views.ServerProtocolViewSet, basename='protocol')

urlpatterns = router.urls + servers_router.urls + endpoints_router.urls
