import sys
import time
import logging
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from events.parse_handler import PacketParserEventHandler


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else './data'
    if not Path('./log').exists():
        Path('./log').mkdir()

    event_handler = PacketParserEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1.0)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()