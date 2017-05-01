# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('cbname', models.CharField(max_length=15)),
                ('cbid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_name', models.CharField(max_length=20)),
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('adm_no', models.IntegerField(primary_key=True, serialize=False)),
                ('phone_no', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('isadmin', models.IntegerField(default=0)),
                ('cbid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Batch')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Course'),
        ),
    ]
