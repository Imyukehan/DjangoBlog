# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-16 06:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Models',
            new_name='Article',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='categroy',
            new_name='category',
        ),
    ]
