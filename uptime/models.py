from django.db import models

from user.models import User


class ServerProtocol(models.Model):
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=100, default='')

    def __str__(self):
        return self.name + " (" + self.slug + ")"


class Server(models.Model):
    hostname = models.CharField(max_length=100, default='')
    protocol = models.ForeignKey(ServerProtocol, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.protocol.slug + "://" + self.hostname

