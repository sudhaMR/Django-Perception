# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImgObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img_file', models.CharField(unique=True, max_length=128)),
                ('img_id', models.IntegerField(default=0)),
                ('img_tags', models.CharField(max_length=320)),
            ],
        ),
        migrations.CreateModel(
            name='UserObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(default=0)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_name', models.CharField(max_length=128)),
            ],
        ),
    ]
