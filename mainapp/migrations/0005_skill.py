# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_delete_person_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('describe', models.TextField()),
            ],
        ),
    ]