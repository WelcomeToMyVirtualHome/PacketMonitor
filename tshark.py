import subprocess 
from pathlib import Path
import json

class TShark():

    @staticmethod
    def run(args):
        subprocess.call(['tshark', *args])
        
    @staticmethod
    def pcapng_to_json(file_in, file_out=None): 
        if file_out is None:
            file_out = f'{Path(file_in).stem}.json'
        subprocess.call(f'tshark -r {file_in} -T json > data/{file_out}', shell=True)
        subprocess.call(['rm', file_in])
        
if __name__ == '__main__':

    if not Path('./data').exists():
        Path('./data').mkdir()

    TShark.run(['-i', 'wlo1', '-c', '100000', '-b', 'duration:5', '-w', 'data/out.pcapng'])    

    paths = [p.name for p in Path().glob('data/*.pcapng')]
    for p in paths:
        TShark.pcapng_to_json('data/' + p)

    