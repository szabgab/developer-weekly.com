#!/usr/bin/env python3
import os
import json
import glob
import logging
import re
import sys

root = os.path.dirname((os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root)
from dw import tools

logging.basicConfig(filename='generate.log', level=logging.DEBUG)

logging.info('Start')

def generate(filename):
    logging.info('processing {}'.format(filename))
    issue = re.search(r'^src/issues/(\d+)\.json$', filename).group(1)
    try:
        data = tools.read_file(filename, issue)
    except Exception as e:
        print('Exception while processing {}'.format(filename))
        print(e)


def run():

    episodes = []
    for filename in glob.glob("src/issues/*.json"):
        if not re.search(r'^src/issues/\d+\.json$', filename):
            raise Exception("Invalid filename {}".format(filename))
        episodes.append( generate(filename) )
run()

# vim: expandtab
