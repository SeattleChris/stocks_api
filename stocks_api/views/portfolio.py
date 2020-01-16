from pyramid_restful.viewsets import APIViewSet
from ..models.schemas import PortfolioSchema
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.response import Response
from ..models import Portfolio, Account
from pyramid.view import view_config
import requests
import json


class PortfolioAPIView(APIViewSet):
    """ Allow us to set what kind of requests will be handled for Portfolio.
    """

    def retrieve(self, request, id=None):
        """ List one of the records with GET (need to pass an id or resource)
        """
        if not id:
            return Response(json='Not Found', status=404)
        try:
            portfolio = Portfolio.one(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        schema = PortfolioSchema()
        data = schema.dump(portfolio).data
        return Response(json={'message': data}, status=200)

    def create(self, request):
        """ Create a new record on POST
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'symbol' not in kwargs:
            return Response(json='Expected value; symbol', status=400)
        # import pdb; pdb.set_trace()
        # if request.authenticated_userid:
        #     account = Account.one(request, request.authenticated_userid)
        #     kwargs['account_id'] = account.id

        try:
            portfolio = Portfolio.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Dupliate Key Error. Symbol already exists', status=409)

        schema = PortfolioSchema()
        data = schema.dump(portfolio).data

        return Response(json=data, status=201)
