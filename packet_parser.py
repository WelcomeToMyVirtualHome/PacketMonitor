from pathlib import Path
import json
import subprocess

class PacketParser:

    @staticmethod
    def parse_json(json):
        layers = json['_source']['layers']
        interface_name = layers['frame']['frame.interface_id_tree']['frame.interface_name']
        timestamp = layers['frame']['frame.time']
        protocols = [p for p in layers['frame']['frame.protocols'].split(':') if p in layers]
        fields = ['%s.src', '%s.dst']
        lines = ''
        for p in protocols:
            for f in fields:
                if f % p in layers[p]:
                    ip = 'address.src' if f == fields[0] else 'address.dst' 
                    lines += f'{{interface_name: {interface_name}, timestamp: "{timestamp}", {ip}: {layers[p][f % p]}}}\n'
        return lines

    @staticmethod
    def to_log(json_file, filename):
        with open(json_file, 'r') as _file:
            json_file = json.load(_file)

        with open(filename, "a+") as _file:
            for j in json_file:
                _file.write(PacketParser.parse_json(j))

if __name__ == '__main__':

    if not Path('./log').exists():
        Path('./log').mkdir()

    files = [p.name for p in Path().glob('./data/*.json')]
    PacketParser.to_log('./data/' + files[0], './log/log.log')