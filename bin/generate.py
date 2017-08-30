#!/usr/bin/env python3
import os
import json
import glob
import logging
import re
from jinja2 import Environment, PackageLoader, FileSystemLoader

logging.basicConfig(filename='generate.log', level=logging.DEBUG)

def generate(filename):
    logging.info('processing {}'.format(filename))
    try:
        with open(filename) as fh:
            data = json.load(fh)
        #with open(filename, 'w') as fh:
        #    json.dump(data, fh, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    except Exception as e:
        print('Exception while processing {}'.format(filename))
        print(e)


def run():
    logging.info('Start')
    env = Environment(
        loader = FileSystemLoader(os.getcwd() + '/templates'),
    )
    
    for filename in glob.glob("src/*.json"):
        if filename == 'src/next.json':
            continue
        if filename == 'src/authors.json':
            continue
        if not re.search(r'^src/\d+\.json$', filename):
            raise Exception("Invalid filename {}".format(filename))
        generate(filename)
    
    template = template = env.get_template('index.html') 
    with open('html/index.html', 'w') as fh:
        fh.write(template.render(next='2017-09-01'))

run()

# vim: expandtab
