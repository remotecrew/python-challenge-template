from flask_marshmallow import Marshmallow
from .models import db, User, Stadium, Match, Seat

ma = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class StadiumSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Stadium

class MatchSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Match

class SeatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Seat
