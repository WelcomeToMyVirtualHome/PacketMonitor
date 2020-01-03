from watchdog.events import FileSystemEventHandler
from packet_parser import PacketParser
import os
import pathlib
import time
import json

class PacketParserEventHandler(PacketParser, FileSystemEventHandler):

    def on_created(self, event):
        time.sleep(0.1) 
        path = pathlib.PosixPath(event.src_path)
        if not event.is_directory and path.name.endswith('.json'):
            log_path = path.cwd() / 'log' / path.name.replace('.json', '.log')
            try:
                self.to_log(event.src_path, log_path)
            except json.decoder.JSONDecodeError as ex:
                with open(log_path, 'w+') as f:
                    f.write(str(ex))
            finally:    
                os.remove(event.src_path)