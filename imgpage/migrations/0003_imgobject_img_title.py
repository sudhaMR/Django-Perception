# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('imgpage', '0002_auto_20150823_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='imgobject',
            name='img_title',
            field=models.CharField(default=datetime.datetime(2015, 9, 10, 10, 31, 8, 712000, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
    ]
