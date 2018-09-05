from ..models.schemas import WeatherLocationSchema
from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.response import Response
from pyramid.view import view_config
from ..models.weather_location import WeatherLocation # this was a guess on my part
import requests


@view_config(route_name='lookup', renderer='json', request_method='GET')
def lookup(request):
    """
    """
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={}'.format(
        request.matchdict['zip_code'],
        'api_key',
    )
    response = requests.get(url)

    return Response(json=response.json(), status=200)


class WeatherLocationAPIView(APIViewSet):
    """ Allow us to set what kind of requests will be handled for stocks api.
    """
    def create(self, request):
        """
        """
        try:
            kwargs - json.loads(request.body)
        except json.JSONDecoderError as e:
            return Response(json-e.msg, status=400)

        if 'zip_code' not in kwargs:
            return Response(json='Expected value; zip_code', status=400)

        try:
            weather = WeatherLocation.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Zip code already exists', status=400)

        schema = WeatherLocationSchema()
        data = schema.dump(weather).data

        return Response(json=data, status=201)


    def retrieve(self, request, id):
        import pdb; pdb.set_trace()
        # http :6543/api/v1/stock/{id}/

        # use the 'id' to lookup the DB resource
        # Make a response and send it to client
        return Response(
            json={'message': f'Give a stock resource for {id}'},
            status=200
        )
    # setup the ablity to parse an id

    def list(self, request):
        """ List all the records with GET
        """
        return Response(json={'message': 'Listing all the stocks'}, status=200)

    def retrieve(self, request, id):
        """ List one of the records with GET (need to pass an id or resource)
        """
        return Response(json={'message': 'Listing one the stocks'}, status=200)

    def create(self, request):
        """ Create a new record on POST
        """
        return Response(json={
            'message': 'Created a new resource'},
            status=201
        )

    def destroy(self, request, id):
        """ Remove a record on DELETE (need to pass an id or resource)
        """
        if not id:
            return Response(json='Not Found', status=404)
        try:
            WeatherLocation.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        return Response(status=204) # remember that a 204 response will ignore and not send a body
        # return Response(json={'message': 'Deleted the record'}, status=204)

