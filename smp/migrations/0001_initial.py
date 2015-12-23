# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auther',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('institution', models.CharField(max_length=30)),
                ('acount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Jounery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('J_name', models.CharField(max_length=30)),
                ('jcount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('MauthorID', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('pdf', models.FileField(upload_to=b'./smp/static/upload')),
                ('pdfname', models.CharField(max_length=30)),
                ('auther', models.ManyToManyField(to='smp.Auther')),
                ('jounery', models.ForeignKey(to='smp.Jounery')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='prauthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=40)),
                ('cate', models.IntegerField(default=5)),
                ('rank', models.CharField(max_length=10)),
                ('gaintime', models.DateField()),
                ('fifthclass', models.ForeignKey(related_name='fifth', to='smp.prauthor')),
                ('firstclass', models.ForeignKey(related_name='first', to='smp.prauthor')),
                ('fourthclass', models.ForeignKey(related_name='fourth', to='smp.prauthor')),
                ('secondclass', models.ForeignKey(related_name='second', to='smp.prauthor')),
                ('thirdclass', models.ForeignKey(related_name='third', to='smp.prauthor')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='zhuanli',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('cate', models.IntegerField()),
                ('number', models.IntegerField()),
                ('institution', models.CharField(max_length=30)),
                ('gaintime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='zhuanzhu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=30)),
                ('gaintime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='zlauthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='zzauthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='zhuanzhu',
            name='fifthclass',
            field=models.ForeignKey(related_name='fifth', to='smp.zzauthor'),
        ),
        migrations.AddField(
            model_name='zhuanzhu',
            name='firstclass',
            field=models.ForeignKey(related_name='first', to='smp.zzauthor'),
        ),
        migrations.AddField(
            model_name='zhuanzhu',
            name='fourthclass',
            field=models.ForeignKey(related_name='fourth', to='smp.zzauthor'),
        ),
        migrations.AddField(
            model_name='zhuanzhu',
            name='secondclass',
            field=models.ForeignKey(related_name='second', to='smp.zzauthor'),
        ),
        migrations.AddField(
            model_name='zhuanzhu',
            name='thirdclass',
            field=models.ForeignKey(related_name='third', to='smp.zzauthor'),
        ),
        migrations.AddField(
            model_name='zhuanzhu',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='zhuanli',
            name='fifthclass',
            field=models.ForeignKey(related_name='fifth', to='smp.zlauthor'),
        ),
        migrations.AddField(
            model_name='zhuanli',
            name='firstclass',
            field=models.ForeignKey(related_name='first', to='smp.zlauthor'),
        ),
        migrations.AddField(
            model_name='zhuanli',
            name='fourthclass',
            field=models.ForeignKey(related_name='fourth', to='smp.zlauthor'),
        ),
        migrations.AddField(
            model_name='zhuanli',
            name='secondclass',
            field=models.ForeignKey(related_name='second', to='smp.zlauthor'),
        ),
        migrations.AddField(
            model_name='zhuanli',
            name='thirdclass',
            field=models.ForeignKey(related_name='third', to='smp.zlauthor'),
        ),
        migrations.AddField(
            model_name='zhuanli',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
