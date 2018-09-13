# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient

def InsertData():
    mc = MongoClient(host='127.0.0.1')
    col = mc['AAAAA']['BBB']
    col.remove({})
    col.insert({"store_id":"A", "item_id":1, "capacity":50 })
    col.insert({"store_id":"A", "item_id":2, "capacity":100})
    col.insert({"store_id":"C", "item_id":1, "capacity":30})
    col.insert({"store_id":"B", "item_id":1, "capacity":20 })
    col.insert({"store_id":"B", "item_id":3, "capacity":40 })

def GroupExample1():
    mc = MongoClient(host='127.0.0.1')
    col = mc['AAAAA']['BBB']

    query = [ {"$match": {"store_id": {"$in":["A","B"] }  }  }, 
             {"$group":  {"_id": "$store_id", "total": {"$sum": "$capacity"} } }  ]

    ret = col.aggregate(query, cursor={ })

    for i in ret:
        print i

def GroupExample2():
    import pymongo
    from pymongo import MongoClient

    mc = MongoClient(host='127.0.0.1')
    col = mc['AAAAA']['BBB']

    query = [ {"$match": {} }, 
             {"$group":  {"_id": {"STORE":"$store_id", "ITEM":"$item_id"}, "total": {"$sum": "$capacity"} } } ]

    ret = col.aggregate(query, cursor={ })

    for i in ret:
        print i

InsertData()
print "Group by example 1"
GroupExample1()
print "Group by example 2"
GroupExample2()

