# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_mysql.models import JSONField

# Create your models here.
class Chili(models.Model):
    name = models.CharField(max_length=100)
    _json = JSONField()
    create_time = models.DateTimeField(u'插入时间',auto_now_add = True,editable = True)
    upadte_time = models.DateTimeField(u'',auto_now = True,null = True)
     
    def __unicode__(self):  # __str__ on Python 3
        return self.name
    
    class Meta:
        db_table = 'chili'