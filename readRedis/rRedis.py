# -*- coding: utf-8 -*-
'''
Created on 2017年11月4日

@author: hylc
'''
import redis
import json
from readMysql.models import Chili

_host = 'sl-us-south-1-portal.1.dblayer.com'
_port = '15884'
_db = '5'
_password = 'WQUQGOKVPAUHCGGS'
client = redis.Redis(_host, _port, _db, _password)

    
def getRandomKey():
   
    randomKey = client.randomkey()
    return randomKey

def getContent(key):
    content = client.smembers(key)
    return content

def add(rRedis):
    key = rRedis.getRandomKey()
    _content = rRedis.getContent(key)
#     json.dumps(content,sort_keys=True,indent =4,separators=(',', ':'),encoding="UTF-8",ensure_ascii=True )
    for c in _content :
        print "key:",key
        print "content :",c
        _save = Chili(name = key, _json = json.dumps(c,sort_keys=True,indent =4,separators=(',', ':'),encoding="UTF-8",ensure_ascii=True ))
        _save.save()
    
    