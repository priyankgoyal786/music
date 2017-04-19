# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=0, max_length=200, null=True, blank=True)),
                ('genres', models.CharField(default=0, max_length=200, null=True, blank=True)),
                ('rating', models.CharField(default=0, max_length=300, null=True, blank=True)),
            ],
        ),
    ]
