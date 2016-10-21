# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acmuu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo', models.CharField(choices=[(1, 'GitHub'), (2, 'Bitbucket'), (3, 'Gitlab')], max_length=2)),
                ('path', models.CharField(help_text='<username>/<project>', max_length=100)),
            ],
        ),
    ]
