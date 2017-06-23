#!/bin/bash

#flow:
#1. create replica sets and specify --shardsvr (so mongos can control it; otherwise it"s just a normal replica set)
#2. create config server replica set for a shard. (Each shard maps to it"s own config server replica set). 
#A shard is a culster of mongos-controlled replica sets. Config server stores metadata of cluster from mongos router.
#3. launch mongos instance.
#4. use mongos to add replica set (those with --shardsvr option) to shard (cluster). 
#
# to create shard databases & collections...
#sh.enableSharding("AAAA") # AAAA:database name
#sh.shardCollection("AAAA.BBBB", {"user":1 })
#sh.shardCollection("AAAA.CCCC", {"user":1 }, {unique:true})

# init mongo001-003(replica set 0), mongo004-006(replica set 1), mongo007-009(config server replica set)
# default port for shardsvr: 27018, configsvr: 27019
docker-compose up -d
echo "check if all mongo connections are ready... then hit enter"
read dummy
docker-compose exec mongo001 mongo --port 27018 /script/init_s0rs0.js # init replica set 0
docker-compose exec mongo004 mongo --port 27018 /script/init_s0rs1.js # init replica set 1
docker-compose exec mongo007 mongo --port 27019 /script/init_s0cfg.js # init config server
# init mongos (also bind config server at launch parameters). It depends on docker-compose.yml configuration info(link to all mongoxxx service) ,so specify all files.
docker-compose -f docker-compose.yml -f docker-compose-mongos.yml up -d
echo "check if mongos connection is ready... then hit enter"
read dummy
docker-compose -f docker-compose.yml -f docker-compose-mongos.yml exec mongos0 mongo /script/add_shard.js # add rs0/rs1 shards to cluster

# creating shard databases & collections...
# sh.enableSharding("AAAA")
# sh.shardCollection("AAAA.BBBB", {"user":1 })
# sh.shardCollection("AAAA.CCCC", {"user":1 }, {unique:true})

