# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeeAsk', '0011_answer_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]