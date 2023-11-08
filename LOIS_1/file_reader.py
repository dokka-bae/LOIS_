from typing import Dict, List

def read_file(file_name : str = '.\\tests\\1' ) -> Dict:
    data : List[str] = []
    with open(file=file_name) as f:
        for line in f:
            data.append(line.strip('\n'))
    data = {
        'values': data[:data.index('')],
        'functions': data[data.index('')+1:]
    }
    return data
