# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pname', models.CharField(max_length=30)),
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_short', models.CharField(max_length=10)),
                ('mrp', models.FloatField(blank=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('product_type', models.CharField(max_length=20)),
                ('brand_name', models.CharField(blank=True, max_length=20)),
                ('spec', models.CharField(blank=True, max_length=200)),
                ('desc', models.CharField(blank=True, max_length=300)),
                ('seller', models.EmailField(blank=True, max_length=70)),
            ],
        ),
    ]
