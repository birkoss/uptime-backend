from rest_framework import routers

from api import views as api_views

router = routers.DefaultRouter()
router.register(r'servers', api_views.ServerViewSet, basename='server')
router.register(r'bots', api_views.BotViewSet, basename='bot')
router.register('auth', api_views.AuthViewSet, basename='auth')
