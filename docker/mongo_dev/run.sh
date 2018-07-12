#!/bin/bash

#flow:
# 1. create replica sets and specify --shardsvr (so mongos can control it; otherwise it"s just a normal replica set)
# 2. create config server replica set for a shard. (Each shard maps to it"s own config server replica set). 
#   A shard is a culster of mongos-controlled replica sets. Config server stores metadata of cluster from mongos router.
# 3. launch mongos instance.
# 4. use mongos to add replica set (those with --shardsvr option) to shard (cluster). 
#

docker-compose up -d

echo " ========== initialzing shard replica sets ... =========="
docker-compose exec pig-mongo-001-test mongo --port 27018 /hostdata/init_scripts/init_clus1_srd1.js # init replica set 0

echo " ========== initialzing config server replica sets ... =========="
docker-compose exec mongo-clus1-cfgsvr1 mongo --port 27019 /hostdata/init_scripts/init_clus1_cfgsvr.js # init config server

echo " ========== adding shards into config servers using one of mongos instnace... =========="
for count in {1..10}
    do
        delay=5
        docker-compose exec pig-gs-001-test mongo --port 27017 /hostdata/init_scripts/add_clus1_srd1.js
        if [ "$?" = 0 ]; then
            echo "add shard succeed!"
            break
        else
            echo "mongos command fails, retry again after $delay seconds ..."
        fi
        sleep $delay
    done

# sh.addShard("clus1:srd1/pig-mongo-001-test:27018")

# creating shard databases & collections...
# sh.enableSharding("AAAA")
# sh.shardCollection("AAAA.BBBB", {"user":1 })
# sh.shardCollection("AAAA.CCCC", {"user":1 }, {unique:true})

