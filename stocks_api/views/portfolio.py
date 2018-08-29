from pyramid_restful.viewsets import APIViewSet
from ..models.schemas import PortfolioSchema
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.response import Response
from ..models import Portfolio
from pyramid.view import view_config
import requests
import json


class PortfolioAPIView(APIViewSet):
    """ Allow us to set what kind of requests will be handled for Portfolio.
    """

    def retrieve(self, request, id):
        """ List one of the records with GET (need to pass an id or resource)
        """
        return Response(json={'message': 'Listing one the stocks'}, status=200)

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
