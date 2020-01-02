#!/bin/bash

docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -it -h elasticsearch --name elasticsearch docker.elastic.co/elasticsearch/elasticsearch:7.5.1
docker run -d -p 5601:5601 -h kibana --name kibana --link elasticsearch:elasticsearch docker.elastic.co/kibana/kibana:7.5.1
# docker run -h logstash --name logstash --link elasticsearch:elasticsearch -it --rm -v "$PWD"/logstash_config:/usr/share/logstash/config docker.elastic.co/logstash/logstash:7.5.1 -f /usr/share/logstash/config/logstash.conf
# docker run --name filebeat -v "$PWD"/filebeat.yml:/usr/share/filebeat/filebeat.yml docker.elastic.co/beats/filebeat:7.5.1
sudo filebeat -e -c filebeat_config/filebeat.yml
