# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imgpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgobject',
            name='img_file',
            field=models.CharField(max_length=128),
        ),
    ]
