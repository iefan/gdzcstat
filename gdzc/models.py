#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class gdzcinfoModel(models.Model):
    modelsn     = models.CharField(null=True, blank=True, max_length=100, verbose_name="编号")
    name        = models.CharField(max_length=100, verbose_name="名称")
    modeltype   = models.CharField(null=True, blank=True, max_length=100, verbose_name="型号")
    modelclass  = models.CharField(max_length=100, verbose_name="类别")
    nums        = models.IntegerField(verbose_name="数量")
    prices      = models.FloatField(verbose_name="价格")
    buydate     = models.DateField(verbose_name="购买日期")
    adminclass  = models.CharField(max_length=100, verbose_name="归属科室")
    adminpp     = models.CharField(null=True, blank=True, max_length=100, verbose_name="责任人")
    demo        = models.TextField(null=True, blank=True, verbose_name="详细备注")
    isuse       = models.CharField(null=True, blank=True, max_length=10, verbose_name="是否在用")

    def __unicode__(self):
        return u"%s　%s　%s　%s　%s　%s　%s　%s %s" % (self.name, self.modeltype, self.modelclass, self.nums, self.prices, self.buydate, self.adminclass, self.adminpp, self.isuse)
