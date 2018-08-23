from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
    """ This is the page returned when user requests our home page.
    """
    message = 'hello world'
    return Response(body=message, status=200)
