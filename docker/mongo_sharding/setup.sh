#!/bin/bash

# only invoked once before mongo environment (config server data / replica set) is setup

#flow:
#1. create replica sets and specify --shardsvr (so mongos can control it; otherwise it"s just a normal replica set)
#2. create config server replica set for a shard. (Each shard maps to it"s own config server replica set). 
#A shard is a culster of mongos-controlled replica sets. Config server stores metadata of cluster from mongos router.
#3. launch mongos instance.
#4. use mongos to add replica set (those with --shardsvr option) to shard (cluster). 
#
# to create shard databases & collections...
# init mongo001-003(replica set 0), mongo004-006(replica set 1), mongo007-009(config server replica set)
# default port for shardsvr: 27018, configsvr: 27019
docker-compose up -d
echo "check if all mongo connections are ready... sleep for 60 seconds"
sleep 60
#read dummy
docker-compose exec mongodb001 mongo --port 27018 /mongo_scripts/init_s1rs1.js # init replica set 0
#docker-compose exec mongodb004 mongo --port 27018 /script/init_s1rs2.js # init replica set 1
docker-compose exec mongocfg001 mongo --port 27019 /mongo_scripts/init_s1cfg.js # init config server
# init mongos (also bind config server at launch parameters). It depends on docker-compose.yml configuration info(link to all mongoxxx service) ,so specify all files.
docker-compose -f docker-compose.yml -f docker-compose-mongos.yml up --no-recreate -d 
echo "check if mongos connection is ready... sleep for 30 seconds"
sleep 30
#read dummy
docker-compose -f docker-compose.yml -f docker-compose-mongos.yml exec mongo mongo /mongo_scripts/add_shard.js # add rs0 shards to cluster

# creating shard databases & collections...
# sh.enableSharding("AAAA")
# sh.shardCollection("AAAA.BBBB", {"user":1 })
# sh.shardCollection("AAAA.CCCC", {"user":1 }, {unique:true})

