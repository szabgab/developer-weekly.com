#!/usr/bin/env python3
import os
import json
import glob
import logging
import re
from jinja2 import Environment, PackageLoader, FileSystemLoader

logging.basicConfig(filename='generate.log', level=logging.DEBUG)

logging.info('Start')
env = Environment(
    loader = FileSystemLoader(os.getcwd() + '/dw/templates'),
)
with open('src/authors.json') as fh:
    authors = json.load(fh)

def generate(filename):
    logging.info('processing {}'.format(filename))
    cnt = re.search(r'^src/issues/(\d+)\.json$', filename).group(1)
    try:
        with open(filename) as fh:
            data = json.load(fh)

        data['id'] = cnt
        data['editor'] = authors[ data['editor'] ]
        for ch in data['chapters']:
            for e in ch['entries']:
               if e['author']:
                   e['author'] = authors[ e['author'] ]
               else:
                   del(e['author'])
 
        template = env.get_template('page.html') 
        with open('html/archive/{}'.format(cnt), 'w') as fh:
            fh.write(template.render(episode=data))
    except Exception as e:
        print('Exception while processing {}'.format(filename))
        print(e)


def run():

    episodes = []
    for filename in glob.glob("src/issues/*.json"):
        if not re.search(r'^src/issues/\d+\.json$', filename):
            raise Exception("Invalid filename {}".format(filename))
        episodes.append( generate(filename) )
    
    template = env.get_template('index.html') 
    with open('html/index.html', 'w') as fh:
        fh.write(template.render(next='2017-09-01'))
# generate each page + generate the latest as e-mail
run()

# vim: expandtab
