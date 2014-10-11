# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0002_userresponse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userresponse',
            old_name='user_requset',
            new_name='user_request',
        ),
        migrations.AddField(
            model_name='user',
            name='tokens',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userrequest',
            name='bounty',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userresponse',
            name='votes',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
