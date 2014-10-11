# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=500)),
                ('votes', models.IntegerField()),
                ('user', models.ForeignKey(to='theapp.User')),
                ('user_requset', models.ForeignKey(related_name=b'responses', to='theapp.UserRequest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
