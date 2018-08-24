from pyramid_restful.routers import ViewSetRouter
from .views.stocks import StocksAPIView
# from .views import CompanyAPView
# above is for later implimatation
# from .views.filename import ClassInViews
# above is the general method


def includeme(config):
    """ Setup the routes we want in our project.
    """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)
    router.register('api/v1/stocks', StocksAPIView, 'stocks')
    # router.register('api/v1/company/', CompanyAPView, 'company')
    # above for later use, following is general usage format.
    # router.register('path/wanted/here/', ClassInViews, 'alias')
