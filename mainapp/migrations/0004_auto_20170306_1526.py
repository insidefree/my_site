# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20170306_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_me',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]