from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StocksAPIView(APIViewSet):
    """ Allow us to set what kind of requests will be handled for stocks api.
    """
    def list(self, request):
        """ List all the records with GET
        """
        return Response(json={'message': 'Listing all the records'}, status=200)

    def retrieve(self, request): 
        """ List one of the records with GET (need to pass an id or resource)
        """
        return Response(json={'message': 'Listing one the records'}, status=200)

    def create(self, request):
        """ Create a new record on POST
        """
        return Response(json={'message': 'Created n new node'}, status=201)

    def destroy(self, request):
        """ Remove a record on DELETE (need to pass an id or resource)
        """
        return Response(json={'message': 'Deleted the record'}, status=204)
