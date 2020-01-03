#!/bin/bash

#docker kill $(docker ps -q -a)
#docker rm $(docker ps -q -a)

docker kill kibana
docker rm kibana

docker kill elasticsearch
docker rm elasticsearch

docker ps -a 