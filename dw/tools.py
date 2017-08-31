import json
import os

root = os.path.dirname((os.path.dirname(os.path.realpath(__file__))))

with open(os.path.join(root, 'src', 'authors.json')) as fh:
    authors = json.load(fh)

def read_file(filename, issue):
    with open(filename) as fh:
        data = json.load(fh)

    data['issue'] = issue
    data['editor'] = authors[ data['editor'] ]
    for ch in data['chapters']:
        for e in ch['entries']:
           if e['author']:
               e['author'] = authors[ e['author'] ]
           else:
               del(e['author'])
    return data

