from django.contrib import admin

from .models import Server, ServerProtocol

admin.site.register(Server)
admin.site.register(ServerProtocol)
