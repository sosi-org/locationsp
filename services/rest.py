
class CODES:
    OK_CREATED_201 = 201
    OK_FINE200 = 200
    OK_204_NO_CONTENT = 204
    ERROR_404 = 404
    DELETE_DONE = OK_204_NO_CONTENT
    """
    A successful response SHOULD be 200 (OK) if the response includes an entity describing the status, 202 (Accepted) if the action has not yet been enacted, or 204 (No Content) if the action has been enacted but the response does not include an entity.
    """

ERROR_404 = CODES.ERROR_404

# Enum not used. It is slow.
POST = 'POST'
DELETE ='DELETE'
GET = 'GET'
PUT = 'PUT'
PATCH = 'PATCH'
OPTIONS ='OPTIONS'
HEAD = 'HEAD'



# Custom responses
from flask import Flask

from flask import jsonify
from flask import abort
from flask import request

import json

#from logger import *

#never call make_response. Always jsonify
from flask import make_response  # for 404

make_response_plain = make_response

make_response = "Uncallable! Never call make_response. Always jsonify."

JSON_MIME='application/json'

def make_response_jsonified(content_dict, rest_code):
    if rest_code == 404:
        if 'error' not in content_dict:
            #log_err("The `error` field is missing in Exception. " + repr(content_dict))
            raise ImplementationError("Error field not set in "+repr(content_dict))
    #log_highlight(repr(content_dict))
    resp = make_response_plain(jsonify(content_dict), rest_code)
    resp.headers.set('Content-Type', JSON_MIME)
    return resp
