#!/bin/bash
docker-compose up -d
echo "wait for all mongo connections to be ready... sleep for 30 seconds"
sleep 30

docker-compose -f docker-compose.yml -f docker-compose-mongos.yml up --no-recreate -d 
echo "check if mongos connection is ready... sleep for 30 seconds"
sleep 30
