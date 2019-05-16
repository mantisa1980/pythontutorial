#!/bin/bash
docker-compose -f docker-compose-mongos.yml -f docker-compose.yml down

sleep 1 
echo "Removing mongod locks..."
rm ~/_docker_/dragon/mongodb001-data/mongod.lock
rm ~/_docker_/dragon/mongodb002-data/mongod.lock
rm ~/_docker_/dragon/mongodb003-data/mongod.lock
