#!/usr/bin/env python3
import os
import json
import glob
import logging
import re
import sys
from jinja2 import Environment, PackageLoader, FileSystemLoader

root = os.path.dirname((os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root)
from dw import tools

logging.basicConfig(filename='generate.log', level=logging.DEBUG)

logging.info('Start')
env = Environment(
    loader = FileSystemLoader(os.getcwd() + '/dw/templates'),
)

def generate(filename):
    logging.info('processing {}'.format(filename))
    issue = re.search(r'^src/issues/(\d+)\.json$', filename).group(1)
    try:
        data = tools.read_file(filename, issue)
        template = env.get_template('page.html') 
        with open('html/archive/{}'.format(issue), 'w') as fh:
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
