# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 18:21
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.postgres.operations import UnaccentExtension


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        UnaccentExtension()
    ]