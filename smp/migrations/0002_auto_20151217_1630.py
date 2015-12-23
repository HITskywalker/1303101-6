# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='middlezl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cate', models.IntegerField()),
                ('author', models.ForeignKey(to='smp.zlauthor')),
            ],
        ),
        migrations.RemoveField(
            model_name='zhuanli',
            name='fifthclass',
        ),
        migrations.RemoveField(
            model_name='zhuanli',
            name='firstclass',
        ),
        migrations.RemoveField(
            model_name='zhuanli',
            name='fourthclass',
        ),
        migrations.RemoveField(
            model_name='zhuanli',
            name='secondclass',
        ),
        migrations.RemoveField(
            model_name='zhuanli',
            name='thirdclass',
        ),
        migrations.AddField(
            model_name='zhuanli',
            name='mzl',
            field=models.ManyToManyField(to='smp.middlezl'),
        ),
    ]
