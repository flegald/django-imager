# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0003_auto_20160413_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='camera',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='photography_type',
            field=models.CharField(choices=[('portrait', 'Portrait'), ('landscape', 'Landscape'), ('nature', 'Nature'), ('family', 'Family'), ('travel', 'Travel'), ('art', 'Art'), ('food', 'Food')], default='art', max_length=255),
        ),
    ]
