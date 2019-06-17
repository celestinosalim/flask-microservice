from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from models import Voter,db
from serializers import VoterSchema, ma
from routes.update import update_voter_blueprint
from routes.create import  create_voter_blueprint
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Init app
app = Flask(__name__)
app.register_blueprint(update_voter_blueprint)
app.register_blueprint(create_voter_blueprint)

limiter = Limiter(app, key_func=get_remote_address,
application_limits=["5 per minute"])

basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lnujflspcwrqms:565ca04b0f1bb7c7153eb44e8872e89172801ab9185cd99ace4dd7135f35c119@ec2-107-20-230-70.compute-1.amazonaws.com:5432/d56amubtoat4hh'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Db
#DATABASE DON'T NEED TO BE INITIALIZE INMMEDIATELY 
#I can call it on models and the init like this.
db.app = app
db.init_app(app)
ma.app = app
ma.init_app(app)


voter_schema = VoterSchema(strict=True)
voters_schema = VoterSchema(many=True, strict=True)


# All Voters
@app.route('/voters', methods=['GET'])
def get_voters():
    all_voters = Voter.query.all()
    result = voters_schema.dump(all_voters)
    return jsonify(result.data)

# Single Voter
@app.route('/voter/<id>', methods=['GET'])
def get_single_voter(id):
    voter = Voter.query.get(id)
    return voter_schema.jsonify(voter)


if __name__ == '__main__':
    app.run(debug=True)
