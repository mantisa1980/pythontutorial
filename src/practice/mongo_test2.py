# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient

mc = MongoClient(host='127.0.0.1', port=27017)
db = mc["User"]
col = db["Wallet"]
col.insert({"name":"John", "coin": 100})

# bulk insert
col_list = [{"name":"Mary", "coin": 200}, {"name":"Ken", "coin": 300}]
col.insert(col_list)

docs = col.find()
print "docs={}, type={}, count={}".format(docs, type(docs), docs.count() )
for i in docs:
    print i

print 'done'
