from flask import Flask, render_template, redirect, abort, request, url_for, Response, jsonify
#import copy
#from datetime import datetime
import os
import json
#import re
import sys

root = os.path.dirname((os.path.dirname(os.path.realpath(__file__))))
sys.path.append(root)
from dw import tools

dwapp = Flask(__name__)
dwapp.config['PROPAGATE_EXCEPTIONS'] = True


with open(os.path.join(root, 'src', 'authors.json')) as fh:
    authors = json.load(fh)

@dwapp.route("/")
def main():
    #cat = _read_json(root + '/html/cat.json')
    return render_template('index.html',
        next='2017-09-01'
    )

@dwapp.route("/archive/<issue>")
def page(issue = None):
    filename = os.path.join(root, 'src', 'issues', issue) + '.json'
    if not os.path.exists(filename):
        return not_found()

    try:
        data = tools.read_file(filename, issue)
        return render_template('page.html', episode=data)
    except Exception as e:
        print('Exception while processing {}'.format(filename))
        print(e)

@dwapp.errorhandler(404)
def not_found(e = None):
    return render_template('404.html',
                       ), 404

 
# vim: expandtab
