from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from models import Voter,db
from serializers import VoterSchema, ma
from routes.update import update_voter_blueprint


# Init app
app = Flask(__name__)
app.register_blueprint(update_voter_blueprint)
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






# Voters Routes

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

# Creating voters
@app.route('/voter', methods=['POST'])
def create_voter():
    for entry in request.json['voters']:
        voter_id = entry['VOTERID']
        last_name = entry['LAST-NAME']
        first_name = entry['FIRST-NAME']
        mid_init = entry["MID-INIT"]
        suffix = entry['SUFFIX']
        date_of_birth = entry["DATE-OF-BIRTH"]
        birth_year = entry["BIRTH YEAR"]
        phone = entry["PHONE"]
        address = entry["ADDR"]
        home_no = entry["HOME-NO"]
        home_apt = entry["HOME-APT"]
        home_street = entry["HOME-STREET"]
        home_dev = entry["HOME-DEV"]
        home_city = entry["HOME-CITY"]
        home_zipcode = entry["HOME-ZIPCODE"]
        county = entry["COUNTY"]
        ed = entry["ED"]
        rd = entry["RD"]
        sd = entry["SD"]
        cn_levy = entry["CNLEVY"]
        wilm = entry["WILM"]
        code_home_city = entry["CODE-HOME-CITY"]
        sch_dist = entry["SCH-DIST"]
        party = entry["PARTY"]
        date_reg = entry["DATE-REG"]
        pp_hist_1 = entry["PP-HIST-1"]
        pp_hist_2 = entry["PP-HIST-2"]
        pr_hist_1 = entry["PR-HIST-1"]
        pr_hist_2 = entry["PR-HIST-2"]
        pr_hist_3 = entry["PR-HIST-3"]
        gen_hist_1 = entry["GEN-HIST-1"] 
        gen_hist_2 = entry["GEN-HIST-2"] 
        gen_hist_3 = entry["GEN-HIST-3"]
        gen_hist_4 = entry["GEN-HIST-4"]
        gen_hist_5 = entry["GEN-HIST-5"]
        sp_hist_1 = entry["SP-HIST-1"]
        sp_hist_2 = entry["SP-HIST-2"]
        sp_hist_3 = entry["SP-HIST-3"]
        schl_hist_1 = entry["SCHL-HIST-1"]
        schl_hist_2 = entry["SCHL-HIST-2"]
        schl_hist_3 = entry["SCHL-HIST-3"]
        schl_hist_4 = entry["SCHL-HIST-4"]
        schl_hist_5 = entry["SCHL-HIST-5"] 
        ref_hist_1 = entry["REF-HIST-1"]
        ref_hist_2 = entry["REF-HIST-2"]
        ref_hist_3 = entry["REF-HIST-3"] 
        ref_hist_4 = entry["REF-HIST-4"]
        ref_hist_5 = entry["REF-HIST-5"]
        mail_no = entry["MAIL-NO"]
        mail_apt = entry["MAIL-APT"]
        mail_street = entry["MAIL-STR"]
        mail_city = entry["MAIL-CITY"]
        mail_state = entry["MAIL-STATE"]
        mail_zip = entry["MAIL-ZIP"]
        date_last_chg = entry["DATE-LAST-CHG"] 
        code_change = entry["CODE-CHANGE"]
        status = entry["STATUS"]
        gender = entry["GENDER"]

        new_voter = Voter(voter_id, last_name, first_name, mid_init, suffix, date_of_birth, 
        birth_year, phone, address, home_no, home_apt, home_street,  home_dev,
        home_city, home_zipcode, county, ed, rd, sd, cn_levy, wilm, code_home_city, 
        sch_dist, party, date_reg, pp_hist_1, pp_hist_2, pr_hist_1, pr_hist_2,
        pr_hist_3, gen_hist_1, gen_hist_2, gen_hist_3, gen_hist_4, gen_hist_5,
        sp_hist_1, sp_hist_2, sp_hist_3, schl_hist_1, schl_hist_2, schl_hist_3,
        schl_hist_4, schl_hist_5, ref_hist_1, ref_hist_2, ref_hist_3, ref_hist_4,
        ref_hist_5, mail_no, mail_apt, mail_street, mail_city, mail_state, mail_zip,
        date_last_chg, code_change, status, gender)

        db.session.add(new_voter)
        db.session.commit()

        return voter_schema.jsonify(new_voter)

# Edit / Update Voter 



# Run Server


if __name__ == '__main__':
    app.run(debug=True)
