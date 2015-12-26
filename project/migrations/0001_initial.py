# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),            ],
            options={
                'db_table': 'member',
            },
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('project_num', models.CharField(unique=True, max_length=50, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x88\xe5\x90\x8c\xe5\x8f\xb7')),
                ('source', models.CharField(max_length=255, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x9d\xa5\xe6\xba\x90', choices=[(b'\xe5\x9b\xbd\xe5\xae\xb6\xe8\x87\xaa\xe7\x84\xb6\xe7\xa7\x91\xe5\xad\xa6\xe5\x9f\xba\xe9\x87\x91', b'1.0'), (b'\xe5\x9b\xbd\xe5\xae\xb6863\xe8\xae\xa1\xe5\x88\x92', b'0.9'), (b'\xe5\x9b\xbd\xe5\xae\xb6\xe7\xa7\x91\xe6\x8a\x80\xe6\x94\xaf\xe6\x92\x91\xe8\xae\xa1\xe5\x88\x92', b'0.8'), (b'\xe5\x9b\xbd\xe9\x98\xb2\xe7\xa7\x91\xe5\xb7\xa5', b'0.7'), (b'\xe7\x9c\x81\xe7\xa7\x91\xe6\x8a\x80\xe6\x94\xbb\xe5\x85\xb3', b'0.65'), (b'\xe4\xbc\x81\xe4\xb8\x9a\xe6\xa8\xaa\xe5\x90\x91', b'0.6')])),
                ('person', models.CharField(max_length=50, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba')),
                ('start_time', models.DateField(verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('end_time', models.DateField(verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('bund', models.FloatField(verbose_name=b'\xe5\x90\x88\xe5\x90\x8c\xe9\xa2\x9d')),
                ('project_member', models.ManyToManyField(to='project.Member')),
            ],
            options={
                'db_table': 'projectstatus',
                'verbose_name': '\u9879\u76ee\u72b6\u6001',
                'verbose_name_plural': '\u9879\u76ee\u72b6\u6001',
            },
        ),
    ]
