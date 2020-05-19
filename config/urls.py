from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from uptime.api.urls import urlpatterns as uptime_router
from user.api.urls import router as user_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(uptime_router)),
    path('api/', include(user_router.urls)),
    path('', TemplateView.as_view(template_name='index.html')),
]
