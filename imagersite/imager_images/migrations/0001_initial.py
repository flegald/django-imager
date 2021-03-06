# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 01:26
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
                ('cover', models.ImageField(default='media/img_files/pupp1.jpg', upload_to=b'')),
                ('title', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('description', models.TextField(blank=True, default=b'', null=True)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('published', models.CharField(choices=[(b'Private', b'Private'), (b'Shared', b'Shared'), (b'Public', b'Public')], default=b'Private', max_length=255)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('description', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('published', models.CharField(choices=[(b'Private', b'Private'), (b'Shared', b'Shared'), (b'Public', b'Public')], default=b'Private', max_length=255)),
                ('img_file', models.ImageField(upload_to=b'img_files')),
                ('in_album', models.ManyToManyField(related_name='photos', to='imager_images.Album')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
