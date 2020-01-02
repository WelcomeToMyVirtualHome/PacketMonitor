#!/bin/bash

docker pull docker.elastic.co/elasticsearch/elasticsearch:7.5.1
docker pull docker.elastic.co/kibana/kibana:7.5.1
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.5.1-amd64.deb
sudo dpkg -i filebeat-7.5.1-amd64.deb