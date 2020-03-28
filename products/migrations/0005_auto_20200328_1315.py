# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-28 13:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200328_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(default='User.fk', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL),
        ),
    ]