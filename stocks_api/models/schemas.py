from marshmallow_sqlalchemy import ModelSchema
from . import WeatherLocation




class WeatherLocationSchema(ModelSchema):
    class Meta:
        model = WeatherLocation
        
