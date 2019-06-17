from flask_marshmallow import Marshmallow
from .models import Voter
from app import ma

class VoterSchema(ma.ModelSchema):
    class Meta:
        model = Voter


