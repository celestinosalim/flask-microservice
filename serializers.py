from flask_marshmallow import Marshmallow
from models import Voter

ma = Marshmallow()

class VoterSchema(ma.ModelSchema):
    class Meta:
        model = Voter

