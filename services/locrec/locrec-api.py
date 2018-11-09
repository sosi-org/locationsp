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


import sys
sys.path.insert(0,'..')

#from ...services import rest as REST
#from .rest as REST
# Parent module '' not loaded, cannot perform relative import
import rest as REST

from rest import ERROR_404

from rest import make_response_jsonified

"""
#import rest as REST
import ..rest as REST
from ..location import Location
from ..location import N2
"""

API_ENDPOINT_URL = "/v1.0"
CLIENT_ENDPOINT_URL = "/v1.0"

app = Flask(__name__)



@app.route('/')
def index():
    # return incorrect_usage_note_response("\"api/\" has nothing to do.", suggested_urls=[CLIENT_ENDPOINT_URL+ "/all-local", CLIENT_ENDPOINT_URL+ "/0/original/"])
    print("INDEX")
    return make_response_jsonified({"error":"errror"}, ERROR_404)


@app.errorhandler(ERROR_404)
def not_found404(exception):
    #log_highlight(repr(exception))
    #log_highlight(str(type(exception)))
    #log_highlight(str(exception))
    #log_highlight(repr(str(exception)))
    description='Not found..'
    return make_response_jsonified({'error': description}, ERROR_404)


@app.route(API_ENDPOINT_URL+'/all-local', methods=[REST.GET])
def invoices_listall():
    return jsonify(images_service.invoices_listall())


@app.route(API_ENDPOINT_URL+'/loc/<int:x>/<int:y>', methods=[REST.POST, REST.GET])
def register_loc(x, y):
    # region_server_no
    # db[serverno]

    #rxy = region(x, y)

    loc = Location(x,y)
    d = dbarray(loc)
    #TODO: loc ORM
    d.append(loc)



if __name__ == '__main__':
    #deployment_self_tests()
    app.run(debug=True, port=9000)
