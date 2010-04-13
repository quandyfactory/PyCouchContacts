#!/usr/bin/env python

"""
A web application in Python, web.py and couchdb application to manage contacts.
"""

__title__ = 'PyCouchContacts'
__version__ = 0.1
__author__ = "Ryan McGreal ryan@quandyfactory.com"
__homepage__ = "http://quandyfactory.com/projects/51/pycouchcontacts"
__copyright__ = "(C) 2010 by Ryan McGreal. Licenced under GNU GPL 2.0\nhttp://www.gnu.org/licenses/old-licenses/gpl-2.0.html"

import httplib2
try: import json
except: import simplejson as json

http = httplib2.Http('.cache')                    
headers = { 'Content-Type': 'application/json' }
url = 'http://localhost:5984'
dbname = 'contacts'

# generic function
def execute(verb, url, content=''):             
    """                                         
    Executes an HTTP request.
    Returns response (dict), content (json)
    """
    if content == '':
        return http.request(url, verb, headers=headers)
    else:
        return http.request(url, verb, content, headers=headers)

def create_database(url, dbname):
    """                          
    Creates a database
    """                 
    return execute('PUT', '%s/%s' % (url, dbname))

def get_databases(url):
    """
    Returns all databases (duh)
    """
    return execute('GET', '%s/_all_dbs' % (url))

def get_database(url, database):
    """
    Returns the details for a database
    """
    return execute('GET', '%s/%s' % (url, database))

def get_docs(url, database):
    """
    Returns the documents in a database
    """
    return execute('GET', '%s/%s/_all_docs' % (url, database))

def display(obj):
    """
    Displays JSON objects nicely.
    * `response` is a dict which we need to dump to formatted JSON.
    * `content` is already JSON, so we load to a dict and then dump to formatted JSON.
    """
    if str(type(obj)) == "<class 'httplib2.Response'>":
        print json.dumps(obj, sort_keys=True, indent=2)
    else:
        print json.dumps(json.loads(obj), sort_keys=True, indent=2)


