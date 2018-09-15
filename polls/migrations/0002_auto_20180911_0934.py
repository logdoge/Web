# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='date',
        ),
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2018, 9, 11, 9, 34, 3, 69016, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
