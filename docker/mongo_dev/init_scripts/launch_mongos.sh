#!/bin/bash

# launch mongos to connect to config servers

mongos --configdb clus1cfg/mongo-clus1-cfgsvr1:27019,mongo-clus1-cfgsvr2:27019,mongo-clus1-cfgsvr3:27019 --bind_ip_all --port 27017 &

# ========== let last command block container ! or it will disappear after launch container ==========
mongos --configdb clus1cfg/mongo-clus1-cfgsvr1:27019,mongo-clus1-cfgsvr2:27019,mongo-clus1-cfgsvr3:27019 --bind_ip_all --port 27018
