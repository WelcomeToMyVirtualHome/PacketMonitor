from pathlib import Path
import json
import subprocess
import dateutil.parser as parser 

class PacketParser:

    @staticmethod
    def parse_json(json):
        layers = json['_source']['layers']
        interface_name = layers['frame']['frame.interface_id_tree']['frame.interface_name']
        timestamp = parser.parse(layers['frame']['frame.time']).isoformat()
        protocols = [p for p in layers['frame']['frame.protocols'].split(':') if p in layers]
        fields = ['%s.src', '%s.dst']
        lines = ''
        for p in protocols:
            for f in fields:
                if f % p in layers[p]:
                    ip = 'address_src' if f == fields[0] else 'address_dst' 
                    lines += f'{{"interface_name": "{interface_name}", "@timestamp": "{timestamp}", "protocol": "{p}", "{ip}": "{layers[p][f % p]}"}}\n'
        return lines

    @staticmethod
    def to_log(json_file, filename):
        with open(filename, "a+") as _file:
            for j in json_file:
                _file.write(PacketParser.parse_json(j))

if __name__ == '__main__':

    if not Path('./log').exists():
        Path('./log').mkdir()

    files = [p.name for p in Path().glob('./data/*.json')]
    [PacketParser.to_log('./data/' + f, './log/log.log') for f in files]