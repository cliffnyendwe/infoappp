# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-16 14:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_stores_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='pic.jpg', upload_to='stores/')),
                ('name_of_schoo', models.CharField(blank=True, max_length=50)),
                ('brach_number', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('school_email_address', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(max_length=500)),
                ('link', models.TextField(null=True, validators=[django.core.validators.URLValidator()])),
            ],
        ),
    ]
