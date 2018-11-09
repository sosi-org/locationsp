# Location receiver
#!locrec/bin/python
"""
Microservice/API for receiving locations:
storage.
"""


from flask import Flask

from flask import jsonify
from flask import request

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


from .. import rest as REST



API_ENDPOINT_URL = "/v1.0"
CLIENT_ENDPOINT_URL = "/v1.0"

app = Flask(__name__)



@app.route('/')
def index():
    # return incorrect_usage_note_response("\"api/\" has nothing to do.", suggested_urls=[CLIENT_ENDPOINT_URL+ "/all-local", CLIENT_ENDPOINT_URL+ "/0/original/"])
    return make_response_jsonified(r, ERROR_404)


@app.errorhandler(ERROR_404)
def not_found404(exception):
    #log_highlight(repr(exception))
    #log_highlight(str(type(exception)))
    #log_highlight(str(exception))
    #log_highlight(repr(str(exception)))
    #description='Not found..'
    #return make_response_jsonified({'error': description}, ERROR_404)

@app.route(API_ENDPOINT_URL+'/all-local', methods=[REST.GET])
def invoices_listall():
    return jsonify(images_service.invoices_listall())

from ../location import Location
from ../location import N2


#dbr = [{}, {}]
#dbr = [[], []]
dbr = map(lambda x: new list(), range(N2))

def dbarray(loc -> Location):
    #rxy = region(loc)
    #dbr[rxy[0]][rxy[1]].append(loc)
    i = regionhash(loc)
    return dbr[i]

@app.route(API_ENDPOINT_URL+'/loc/<int:x>/<int:y>', methods=[REST.POST])
def register_loc(x, y):
    # region_server_no
    # db[serverno]

    #rxy = region(x, y)

    loc = Location(x,y)
    d = dbarray(loc)
    #TODO: loc ORM
    d.append(loc)

import numpy as np

def all_locs_numpy(hash):
    a = np.toarray(dbr[hash])
    return a

# never use
def all_locs_numpy_total(hash):
    for hash in range(len(dbr)):
        a = np.toarray(dbr[hash])
        raise NotImplemented()
