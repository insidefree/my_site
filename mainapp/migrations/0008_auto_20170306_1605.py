# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 14:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20170306_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='content',
            new_name='story',
        ),
    ]
