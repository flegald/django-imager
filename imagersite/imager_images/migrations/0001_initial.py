# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 02:16
from __future__ import unicode_literals

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
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=b'', max_length=100)),
                ('description', models.CharField(default=b'', max_length=200)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('published', models.CharField(choices=[(b'Private', b'Private'), (b'Shared', b'Shared'), (b'Public', b'Public')], default=b'Private', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=b'', max_length=100)),
                ('description', models.CharField(default=b'', max_length=200)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('published', models.CharField(choices=[(b'Private', b'Private'), (b'Shared', b'Shared'), (b'Public', b'Public')], default=b'Private', max_length=7)),
                ('in_album', models.ManyToManyField(related_name='photos', to='imager_images.Album')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='contains',
            field=models.ManyToManyField(related_name='albums', to='imager_images.Photo'),
        ),
        migrations.AddField(
            model_name='album',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL),
        ),
    ]