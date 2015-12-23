# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smp', '0002_auto_20151217_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='middlepr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cate', models.IntegerField()),
                ('author', models.ForeignKey(to='smp.prauthor')),
            ],
        ),
        migrations.CreateModel(
            name='middlezz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cate', models.IntegerField()),
                ('author', models.ForeignKey(to='smp.zzauthor')),
            ],
        ),
        migrations.RemoveField(
            model_name='prize',
            name='fifthclass',
        ),
        migrations.RemoveField(
            model_name='prize',
            name='firstclass',
        ),
        migrations.RemoveField(
            model_name='prize',
            name='fourthclass',
        ),
        migrations.RemoveField(
            model_name='prize',
            name='secondclass',
        ),
        migrations.RemoveField(
            model_name='prize',
            name='thirdclass',
        ),
        migrations.RemoveField(
            model_name='zhuanzhu',
            name='fifthclass',
        ),
        migrations.RemoveField(
            model_name='zhuanzhu',
            name='firstclass',
        ),
        migrations.RemoveField(
            model_name='zhuanzhu',
            name='fourthclass',
        ),
        migrations.RemoveField(
            model_name='zhuanzhu',
            name='secondclass',
        ),
        migrations.RemoveField(
            model_name='zhuanzhu',
            name='thirdclass',
        ),
        migrations.AddField(
            model_name='prize',
            name='mpr',
            field=models.ManyToManyField(to='smp.middlepr'),
        ),
        migrations.AddField(
            model_name='zhuanzhu',
            name='mzz',
            field=models.ManyToManyField(to='smp.middlezz'),
        ),
    ]
