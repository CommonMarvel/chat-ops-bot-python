#!/bin/bash

docker pull jianminhuang/devops-bot:2
docker-compose stop devops-bot-2
docker-compose rm -f devops-bot-2
docker-compose up -d devops-bot-2

sleep 5s

docker-compose logs devops-bot-2
