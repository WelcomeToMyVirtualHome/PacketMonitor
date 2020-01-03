# PacketMonitor

Download required docker images of Elasticsearch and Kibana and Filebeat deb package: `./install.sh`

Start Elasticsearch, Kibana and Filebeat: `./run_elk.sh`

Import dashboard in `export.ndjson` to Kibana.

Specify interface to capture with `-i` in `run_tshark.sh`. Start capturing packets with TShark: `./run_tshark.sh`

Run file parser with: `python file_listener.py`
