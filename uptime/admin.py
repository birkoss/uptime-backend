from django.contrib import admin

from .models import Bot, Ping, Endpoint, Server, ServerProtocol

admin.site.register(Ping)
admin.site.register(Endpoint)
admin.site.register(Server)
admin.site.register(Bot)
admin.site.register(ServerProtocol)
