# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=0, max_length=200, null=True, blank=True)),
                ('genre', models.CharField(default=0, max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='music',
            name='genres',
            field=models.ForeignKey(related_name='genres', blank=True, to='musicapp.Genres', null=True),
        ),
    ]
