# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 07:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20171111_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_cost',
            new_name='item_price',
        ),
    ]