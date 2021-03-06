from flask import Flask, render_template, redirect, abort, request, url_for, Response, jsonify, send_from_directory
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


#with open(os.path.join(root, 'src', 'authors.json')) as fh:
#    authors = json.load(fh)
with open(os.path.join(root, 'src', 'next.json')) as fh:
    next = json.load(fh)
with open(os.path.join(root, 'src', 'issues.json')) as fh:
    issues = json.load(fh)

@dwapp.route("/")
def main():
    return render_template('index.html',
        next = next['date'],
        last = issues[-1],
    )

@dwapp.route("/archive/<issue>")
def page(issue = None, email = None):
    filename = os.path.join(root, 'src', 'issues', issue) + '.json'
    if not os.path.exists(filename):
        return not_found()

    try:
        data = tools.read_file(filename, issue)
        return render_template('page.html',
            episode=data,
            email=email
        )
    except Exception as e:
        print('Exception while processing {}'.format(filename))
        print(e)

@dwapp.route("/email")
def email():
   return page(issues[-1]['issue'], True)


@dwapp.errorhandler(404)
def not_found(e = None):
    return render_template('404.html',
    ), 404

# Web server should be configured to serve these directly
@dwapp.route('/img/<path:path>')
def send_img(path):
    return send_from_directory(os.path.join(root, 'html', 'img'), path)
 
# vim: expandtab
