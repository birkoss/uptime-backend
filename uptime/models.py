import uuid

from django.db import models

from user.models import User


class Bot(models.Model):
    name = models.CharField(max_length=100, default='')
    key = models.SlugField(max_length=32, default='', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.key.strip():
            self.key = uuid.uuid1().hex
        super(Bot, self).save()


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


class Endpoint(models.Model):
    server = models.ForeignKey(Server, on_delete=models.PROTECT)
    url = models.CharField(max_length=100, default='')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.server.__str__() + self.url


class Ping(models.Model):
    endpoint = models.ForeignKey(Endpoint, on_delete=models.PROTECT)
    bot = models.ForeignKey(Bot, on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)

    response_code = models.SmallIntegerField(db_index=True)
    response_time = models.DecimalField(
        max_digits=10, decimal_places=6
    )  # 1234.123456
    response_headers = models.TextField()
    response_body = models.TextField()

    class Meta:
        ordering = ('-date_added', )

    def __str__(self):
        return self.endpoint.__str__() + " (" + str(self.response_code) + ") = " + str(self.response_time)
