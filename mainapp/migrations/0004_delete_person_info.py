# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 13:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_person_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person_info',
        ),
    ]
