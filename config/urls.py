from django.contrib import admin
from django.urls import include, path

from api.urls import router as api_router
from user.api.urls import router as user_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_router.urls)),
    path('api/', include(user_router.urls)),
]
