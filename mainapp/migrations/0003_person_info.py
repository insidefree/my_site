# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_company_study_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('skills', models.TextField()),
            ],
        ),
    ]