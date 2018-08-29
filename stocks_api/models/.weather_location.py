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


class WeatherLocation(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    zip_code = Column(Integer, unique=True, nullable=False)

    data_created = Column(DateTime, default=dt.now())
    data_updated = Column(DateTime, default=dt.now(), enupdate=dt.now())

    @classmethod
    def new(cls, request, **kwargs):
        if request.dbsession is None:
            raise DBAPIError

        # weather = WeatherLocation({'name': 'some name', 'zip_code': '98038})
        weather = cls(**kwargs)
        request.dbsession.add(weather)

        return request.dbsession.query(cls).filter(
            cls.zip_code == kwargs['zip_code']).one_or_none()

    @classmethod
    def all(cls, request):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).all()
        # maybe would want first 10, reference to the next 10

    @classmethod
    def one(cls, request, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)

    @classmethod
    def remove(cls, request=None, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk).delete()




