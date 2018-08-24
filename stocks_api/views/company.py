from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class CompanyAPIView(APIViewSet):
    """
    """
    def retrieve(self, request, id):
        # http :6543/api/v1/company/{id}/
        return Response(jason={'message': f'Provide a single resorce for {id}'})

    def list(self, request):
        # http :6543/api/v1/company/
        pass
