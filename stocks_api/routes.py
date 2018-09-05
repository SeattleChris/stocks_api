from pyramid_restful.routers import ViewSetRouter
from .views import StocksAPIView, CompanyAPIView, PortfolioAPIView
# from .views directory works thanks to __all__ in the views directory __init__
# Otherwise we would need .views.filename


def includeme(config):
    """ Setup the routes we want in our project.
    """
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    # config.add_route('lookup', 'api/v1/lookup/{zip_code}')

    router = ViewSetRouter(config, trailing_slash=False)
    router.register('api/v1/stocks', StocksAPIView, 'stocks')
    router.register('api/v1/company', CompanyAPIView, 'company')
    router.register('api/v1/portfolio', PortfolioAPIView, 'portfolio')
    # router.register('api/v1/auth', AuthAPIView, 'auth')
    # router.register('path/wanted/here', ClassInViews, 'alias')
