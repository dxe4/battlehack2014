# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0004_auto_20141011_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='city',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userrequest',
            name='country',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userrequest',
            name='country_code',
            field=models.CharField(default=None, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userrequest',
            name='location',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
    ]
