# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from readMysql.tasks import add

# Create your views here.
def viewArticle(request):
    text = "Displaying article Number : working"
    #a = build_job().delay()
    r = add.delay(2,2)
    print r
    return HttpResponse(text)