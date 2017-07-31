# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient

mc = MongoClient(host='127.0.0.1', port=27017)
db = mc["User"]
col = db["Wallet"]

upsert_flag = False
new_flag = False
 
col.remove()
print "update result=", col.update({"name":"John"},{"$set":{"coin":50} } , upsert=upsert_flag)
print "find_and_modify result=", col.find_and_modify({"name":"Mark"},{"$set":{"coin":100} } , upsert=upsert_flag, new=new_flag)

docs = col.find()
print "documents after $set"
for i in col.find():
    print i

col.update({"name":"John","coin":{"$gte":100 } },{"$inc":{"coin":-100}})
col.update({"name":"Mark"},{"$inc":{"coin":100}})
print "documents after $inc"
for i in col.find():
    print i

print 'done'
