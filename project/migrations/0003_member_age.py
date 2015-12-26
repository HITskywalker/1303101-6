# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20151119_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.CharField(max_length=10, verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84'),
            preserve_default=False,
        ),
    ]
