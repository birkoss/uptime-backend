# Generated by Django 3.0.6 on 2020-05-18 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('key', models.SlugField(blank=True, default='', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='', max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServerProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('slug', models.SlugField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(default='', max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('protocol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uptime.ServerProtocol')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('response_code', models.SmallIntegerField(db_index=True)),
                ('response_time', models.DecimalField(decimal_places=6, max_digits=10)),
                ('response_headers', models.TextField()),
                ('response_body', models.TextField()),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uptime.Bot')),
                ('endpoint', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uptime.Endpoint')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
        migrations.AddField(
            model_name='endpoint',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uptime.Server'),
        ),
    ]
