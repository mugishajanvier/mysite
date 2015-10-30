# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherCondition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city_name', models.CharField(max_length=64)),
                ('high_temperature', models.CharField(max_length=3)),
                ('low_temperature', models.CharField(max_length=3)),
                ('day_perc_ch', models.CharField(max_length=3)),
                ('night_perc_ch', models.CharField(max_length=3)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
