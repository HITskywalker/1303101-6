# coding: utf-8
from django.db import models
ProjectSource = (
    ('1.0','国家自然科学基金'),
    ('0.9','国家863计划'),
    ('0.85','国家科技支撑计划'),
    ('0.8','国防科工'),
    ('0.75','省科技攻关'),
    ('0.7','企业横向'),
)
class CommonInfo(models.Model):
    name = models.CharField('项目名称',max_length=255)
    project_num = models.CharField('项目合同号',max_length=50,unique=True)
    source = models.CharField('项目来源',max_length=255,choices=ProjectSource)
    person  = models.CharField('项目负责人',max_length=50)
    bund = models.FloatField('合同额')
    start_time = models.DateField('开始时间')
    end_time = models.DateField('结束时间')
    class Meta:
        abstract = True

class Member(models.Model):
    name = models.CharField('姓名',max_length=50)
    age = models.CharField('年龄',max_length=10)
    class Meta:
        db_table = 'member'

    def __unicode__(self):
        return self.name

class Project(CommonInfo):

    project_member = models.ManyToManyField(Member)

    class Meta:
        db_table = 'project'
        verbose_name = '科研项目'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class ProjectCheck(CommonInfo):

    check_time = models.DateField('验收时间')
    check_org = models.CharField('验收组织',max_length=100)
    check_text = models.TextField('验收结论',default='')

    class Meta:
        db_table = 'projectcheck'
        verbose_name = '项目验收'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class ProjectIdentify(CommonInfo):
    identify_time = models.DateField('鉴定时间')
    identify_org = models.CharField('鉴定组织',max_length=100)
    identify_text = models.TextField('鉴定结论',default='')

    class Meta:
        db_table = 'projectidentify'
        verbose_name = '项目鉴定'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
