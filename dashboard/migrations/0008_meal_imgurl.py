# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20161216_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='imgurl',
            field=models.URLField(default='http://www.driftstories.com/wp-content/uploads/2015/12/chicken-curry2.jpg'),
            preserve_default=False,
        ),
    ]