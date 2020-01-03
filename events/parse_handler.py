from watchdog.events import FileSystemEventHandler
from packet_parser import PacketParser
import os
import pathlib
import time
import json
import subprocess

class PacketParserEventHandler(PacketParser, FileSystemEventHandler):

    def on_created(self, event):
        time.sleep(0.1) 
        path = pathlib.PosixPath(event.src_path)
        if not event.is_directory and path.name.endswith('.pcapng'):
            result = subprocess.run(['tshark', '-r', str(path), '-T', 'json'], stdout=subprocess.PIPE)
            _json = json.loads(result.stdout)
            log_path = path.cwd() / 'log' / path.name.replace('.pcapng', '.log')
            try:
                self.to_log(_json, log_path)
            except json.decoder.JSONDecodeError as ex:
                with open(log_path, 'a+') as f:
                    f.write(str(ex))
            finally:    
                os.remove(event.src_path)