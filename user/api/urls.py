from rest_framework import routers

from . import views as user_views

router = routers.DefaultRouter()
router.register('auth', user_views.AuthViewSet, basename='auth')
