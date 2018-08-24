from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StocksAPIView(APIViewSet):
    """ Allow us to set what kind of requests will be handled for stocks api.
    """
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
        return Response(json={'message': 'Deleted the record'}, status=204)
