# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0003_auto_20141011_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresponse',
            name='accepted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='user',
            field=models.ForeignKey(related_name=b'user_requests', to='theapp.User'),
        ),
        migrations.AlterField(
            model_name='userresponse',
            name='user',
            field=models.ForeignKey(related_name=b'user_responses', to='theapp.User'),
        ),
    ]
