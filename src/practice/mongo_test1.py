# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient

mc = MongoClient(host='127.0.0.1', port=27017)
db = mc["User"]
col = db["Wallet"]
docs = col.find()

print "docs={}, type={}, count={}".format(docs, type(docs), docs.count() )

for i in docs:
    print i

print 'done'
