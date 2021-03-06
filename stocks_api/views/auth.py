# from pyramid_restful.viewsets import APIViewSet
# from sqlalchemy.exc import IntegrityError
# from pyramid.response import Response
# from ..models import Account
# import json


# class AuthAPIView(APIViewSet):
#     """ This class displays the api endpoint message.
#         It is not built out yet, as it needs
#         actual functionality besides just sending jsons.
#     """
    # import pdb; pdb.set_trace()

    # def create(self, request, auth=None):
    #     """ This creates a new user session. Two possible subpaths: register and login.
    #         New users visit register, create an account, this is stored in DB
    #         When a user inputs on login, it checks user password in the DB.
    #         If successful, start session using this user's permissions.
    #     """
    #     data = json.loads(request.body)
    #     if auth == 'register':
    #         try:
    #             user = Account.new(
    #                 request,
    #                 data['email'],
    #                 data['password'],
    #             )
    #         except (IntegrityError, KeyError):
    #             return Response(json='Bad Request', status=400)

    #         return Response(
    #             json_body={
    #                 'token': request.create_jwt_token(
    #                     user.email,
    #                     roles=[role.name for role in user.roles],
    #                     userName=user.email,
    #                 )
    #             },
    #             status=201
    #         )

    #     if auth == 'login':
    #         authenticated = Account.check_credentials(request, data['email'], data['password'])
    #         if authenticated:
    #             return Response(
    #                 json_body={
    #                 'token': request.create_jwt_token(
    #                     authenticated.email,
    #                     roles=[role.name for role in authenticated.roles],
    #                     userName=authenticated.email,
    #                 )
    #             },
    #             status=201)
    #         else:
    #             return Response(json='Not Authorized!', status=401)

    #     return Response(json='AUTH Not Found', status=404)
