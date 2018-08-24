from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
    """ This is the page returned when user requests our home page.
    """
    message = '''
        GET / - Base API route\n
        POST /api/v1/auth - Register a new account\n
        GET /api/v1/auth - Login to an existing account\n
        GET /api/v1/stocks/ - Retrieve all stocks\n
        GET /api/v1/stocks/<id>/ - Retrieve specific stocks\n
        POST /api/v1/stocks/ - Create a new stocks resource\n
        DELETE /api/v1/stocks/<id>/ Remove existing stocks resource\n
    '''
    return Response(body=message, content_type="text/plain", status=200)
