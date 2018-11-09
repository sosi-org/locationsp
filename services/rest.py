
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
