# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_remove_work_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=10)),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='About_me',
        ),
    ]
