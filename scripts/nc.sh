#! /bin/bash

net=$(docker network ls | grep tp0_testing_net)
if [ -z "$net" ]
then
    echo "Docker network not found. Run 'make docker-compose-up' to set up the environment."
    exit 1
fi

PORT=$(cat server/config.ini | awk '$1 == "SERVER_PORT" {print $3}')
RES=$(echo HEALTH CHECK | docker run -i --rm --network=tp0_testing_net --name=ncs netcat -t server $PORT 2> /dev/null)
if [ "$RES" != "HEALTH CHECK" ]
then
    echo "Server not running"
    exit 1
fi
echo "Server is running and healthy"
