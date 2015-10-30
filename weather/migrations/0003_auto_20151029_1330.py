# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20151029_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weathercondition',
            old_name='day_perc_ch',
            new_name='humidity',
        ),
        migrations.RenameField(
            model_name='weathercondition',
            old_name='high_temperature',
            new_name='temperature',
        ),
        migrations.RenameField(
            model_name='weathercondition',
            old_name='low_temperature',
            new_name='visibility',
        ),
        migrations.RemoveField(
            model_name='weathercondition',
            name='night_perc_ch',
        ),
    ]
