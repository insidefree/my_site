# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20170305_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_me',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
