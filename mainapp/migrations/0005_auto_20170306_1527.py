# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20170306_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='study',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
