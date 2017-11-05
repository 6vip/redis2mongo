# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from readMysql.models import Chili
# Register your models here.

class ChiliAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name','_json','create_time')
    search_fields = ('name',)   #添加快速查询栏
#     list_filter = ['_json', ]
    
admin.site.register(Chili,ChiliAdmin)

