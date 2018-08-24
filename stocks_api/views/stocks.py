from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StocksAPIView(APIViewSet):
    """ Allow us to set what kind of requests will be handled for stocks api.
    """
    # setup the ablity to parse an id
    id = 1

    def list(self, request):
        """ List all the records with GET
        """
        return Response(json={'message': 'Listing all the stocks'}, status=200)

    def retrieve(self, request):
        """ List one of the records with GET (need to pass an id or resource)
        """
        return Response(json={'message': 'Listing one the stocks'}, status=200)

    def create(self, request, id):
        """ Create a new record on POST
        """
        # return Response(json={'message': f'Created a new resource for {id}'}, status=201)
        return Response(json={'message': 'Created n new node'}, status=201)

    def destroy(self, request, id):
        """ Remove a record on DELETE (need to pass an id or resource)
        """
        return Response(json={'message': 'Deleted the record'}, status=204)
