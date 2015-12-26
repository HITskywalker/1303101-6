# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auther',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('institution', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Jounery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('J_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('pdf', models.FileField(upload_to=b'./upload/')),
                ('pdfname', models.CharField(max_length=30)),
                ('auther', models.ManyToManyField(to='smp.Auther')),
                ('jounery', models.ManyToManyField(to='smp.Jounery')),
            ],
        ),
    ]
