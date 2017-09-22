#!/usr/bin/env python3
import json
import glob

# format the json files

def tidy(filename):
    try:
        with open(filename) as fh:
            data = json.load(fh)
        with open(filename, 'w') as fh:
            json.dump(data, fh, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    except Exception as e:
        print('Exception while processing {}'.format(filename))
        print(e)

for filename in glob.glob("src/*.json"):
    if filename == 'src/next.json':
        continue
    if filename == 'src/person.json':
        continue
    tidy(filename)

for filename in glob.glob("src/issues/*.json"):
    tidy(filename)

# vim: expandtab

