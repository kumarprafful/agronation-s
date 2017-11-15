# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 18:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20171113_0738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(default='', max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'ordering': ('item_type',),
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('item_name',)},
        ),
        migrations.AddField(
            model_name='item',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.RemoveField(
            model_name='item',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_type',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='store.Category'),
        ),
        migrations.AlterIndexTogether(
            name='item',
            index_together=set([('id', 'slug')]),
        ),
    ]
