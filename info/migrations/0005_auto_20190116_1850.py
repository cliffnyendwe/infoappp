# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-16 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_schools'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schools',
            old_name='name_of_schoo',
            new_name='name_of_school',
        ),
    ]
