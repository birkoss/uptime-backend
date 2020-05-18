from rest_framework import routers

from . import views as api_views

router = routers.DefaultRouter()
router.register(r'servers', api_views.ServerViewSet, basename='server')
router.register(r'endpoints', api_views.EndpointViewSet, basename='endpoint')
router.register(r'bots', api_views.BotViewSet, basename='bot')