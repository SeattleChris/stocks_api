from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)
from .meta import Base


class Stock(Base):
    """ This creates instances of a company stock, using information from IEX API.
        We get company name, symbol, exchange, indusry, website, description, ceo,
        stock type, and sector. We also track when this info was put into our DB
        and when it was last updated in our DB
    """
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    symbol = Column(Text, nullable=False)  # is this the best thing to lookup from 3rd party API?
    company_name = Column(Text)
    exchange = Column(Text)
    industry = Column(Text)
    website = Column(Text)
    description = Column(Text)
    ceo = Column(Text)
    issue_type = Column(Text)
    sector = Column(Text)
    data_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    @classmethod
    def all(cls, request):
        """ GET all stocks we have in our DB
        """
        # maybe name list
        if request.dbsession is None:
            raise DBAPIError
        return request.dbsession.query(cls).all()

    @classmethod
    def one(cls, request=None, pk=None):
        """  Retrieve a single instance from the database by the primary key
            for that record. pk is used for the primary key
        """
        if request.dbsession is None:
            raise DBAPIError
        return request.dbsession.query(cls).get(pk)

    @classmethod
    def new(cls, request, **kwargs):
        """ Create a single new instance of the Portfolio class
        """
        if request.dbsession is None:
            raise DBAPIError
        # portfolio = cls(**kwargs)
        # request.dbsession.add(portfolio)
        # return True
        stock = cls(**kwargs)
        request.dbsession.add(stock)
        return request.dbsession.query(cls).filter(
            cls.symbol == kwargs['symbol']).one_or_none()

    @classmethod
    def destroy(cls, request=None, pk=None):
        """ Remove a single instance from the database by the primary key for that record
        """
        if request.dbsession is None:
            raise DBAPIError
        # return request.dbsession.query(cls).get(pk).delete()
        return request.dbsession.query(cls).filter(
            cls.accounts.email == request.authenticated_userid
            ).filter(cls.id == pk).delete()
