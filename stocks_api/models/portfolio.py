from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    Float,
    ForeignKey
)
from .meta import Base


class Portfolio(Base):
    """ Creates a new portfolio and DB table.
    """
    __tablename__ = 'portfolios'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    accounts = relationship('Account', back_populates='portfolio')

    @classmethod
    def one(cls, request=None, pk=None):
        """  Retrieve a single instance from the database by the primary key
            for that record
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
        portfolio = cls(**kwargs)
        request.dbsession.add(portfolio)
        # return True
        return request.dbsession.query(cls).filter(
            cls.name == kwargs['name']).one_or_none()





