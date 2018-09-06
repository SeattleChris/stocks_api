from ..models.schemas import PortfolioSchema, StockSchema
from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.response import Response
from ..models import Portfolio, Stock
from pyramid.view import view_config
import requests
import json

API_URL = 'https://api.iextrading.com/1.0/'


@view_config(route_name='lookup', renderer='json', request_method='GET')
def lookup(request):
    """ Listen for a request to lookup a stock company
    """
    # see 11:57 of last lecture hour of day 11
    symbol = request.matchdict['symbol']
    url = f'{API_URL}stock/{symbol}/company'
    response = requests.get(url)

    return Response(json=response.json(), status=200)


class StocksAPIView(APIViewSet):
    """ Allow us to set what kind of requests will be handled for stocks api.
    """
    def create(self, request):
        """ Create a new record on POST
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'symbol' not in kwargs:
            return Response(json='Expected value; symbol', status=400)
        try:
            stock = Stock.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Dupliate Key Error. Symbol already exists', status=409)

        schema = StockSchema()
        data = schema.dump(stock).data
        return Response(json=data, status=201)

    def retrieve(self, request, id=None):
        """ Use the 'id' to lookup the DB resource
            Make a response and send it to client.
            http :6543/api/v1/stock/{id}/
        """
        if not id:
            return Response(json='Not Found', status=404)

        target = Stock.one(request, id)
        if not target:
            return Response(json='Not Found', status=404)
        schema = StockSchema()
        data = schema.dump(target).data
        return Response(json=data, status=200)
        # return Response(
        #     json={'message': f'Give a stock resource for {id}'},
        #     status=200
        # )

    def list(self, request):
        """ List all the records with GET
        """
        target = Stock.all(request)
        schema = StockSchema()
        data = [schema.dump(each) for each in target]
        return Response(json=data, status=200)
        # return Response(json={'message': 'Listing all the stocks'}, status=200)

    def destroy(self, request, id=None):
        """ Remove a record on DELETE (need to pass an id or resource)
        """
        if not id:
            return Response(json='Not Found', status=404)
        try:
            Stock.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)
        return Response(status=204)
