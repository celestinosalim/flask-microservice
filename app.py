from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

from .models import Voter
from .serializers import VoterSchema

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lnujflspcwrqms:565ca04b0f1bb7c7153eb44e8872e89172801ab9185cd99ace4dd7135f35c119@ec2-107-20-230-70.compute-1.amazonaws.com:5432/d56amubtoat4hh'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Db
db = SQLAlchemy(app)
ma = Marshmallow(app)


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
@app.route('/voter/<id>', methods=['PUT'])
def update_voter(id):
    voter = Voter.query.get(id)
    voter_id = request.json['VOTERID']
    last_name = request.json['last_name']
    first_name = request.json['first_name']
    mid_init = request.json['mid_init']
    suffix = request.json['suffix']
    date_of_birth = request.json['date_of_birth']
    birth_year = request.json['birth_year']
    phone = request.json['phone']
    address = request.json['address']
    home_no = request.json['home_no']
    home_apt = request.json['home_apt']
    home_street = request.json['home_street']
    home_dev = request.json['home_dev']
    home_city = request.json['home_city']
    home_zipcode = request.json['home_zipcode']
    county = request.json['county']
    ed = request.json['ed']
    rd = request.json['rd']
    sd = request.json['sd']
    cn_levy = request.json['cn_levy']
    wilm = request.json['wilm']
    code_home_city = request.json['code_home_city']
    sch_dist = request.json['sch_dist']
    party = request.json['party']
    date_reg = request.json['date_reg']
    pp_hist_1 = request.json['pp_hist_1']
    pp_hist_2 = request.json['pp_hist_2']
    pr_hist_1 = request.json['pr_hist_1']
    pr_hist_2 = request.json['pr_hist_2']
    pr_hist_3 = request.json['pr_hist_3']
    gen_hist_1 = request.json['gen_hist_1'] 
    gen_hist_2 = request.json['gen_hist_2'] 
    gen_hist_3 = request.json['gen_hist_3']
    gen_hist_4 = request.json['gen_hist_4']
    gen_hist_5 = request.json['gen_hist_5']
    sp_hist_1 = request.json['sp_hist_1']
    sp_hist_2 = request.json['sp_hist_2']
    sp_hist_3 = request.json['sp_hist_3']
    schl_hist_1 = request.json['schl_hist_1']
    schl_hist_2 = request.json['schl_hist_2']
    schl_hist_3 = request.json['schl_hist_3']
    schl_hist_4 = request.json['schl_hist_4']
    schl_hist_5 = request.json['schl_hist_5'] 
    ref_hist_1 = request.json['ref_hist_1']
    ref_hist_2 = request.json['ref_hist_2']
    ref_hist_3 = request.json['ref_hist_3'] 
    ref_hist_4 = request.json['ref_hist_4']
    ref_hist_5 = request.json['ref_hist_5']
    mail_no = request.json['mail_no']
    mail_apt = request.json['mail_apt']
    mail_street = request.json['mail_street']
    mail_city = request.json['mail_city']
    mail_state = request.json['mail_state']
    mail_zip = request.json['mail_zip']
    date_last_chg = request.json['date_last_chg'] 
    code_change = request.json['code_change']
    status = request.json['status']
    gender = request.json['gender']

    voter.voter_id = voter_id
    voter.last_name = last_name
    voter.first_name = first_name
    voter.mid_init = mid_init
    voter.suffix = suffix
    voter.date_of_birth = date_of_birth
    voter.birth_year = birth_year
    voter.phone = phone
    voter.address = address
    voter.home_no = home_no
    voter.home_apt = home_apt
    voter.home_street = home_street
    voter.home_dev = home_dev
    voter.home_city = home_city
    voter.home_zipcode = home_zipcode
    voter.county = county
    voter.ed = ed
    voter.rd = rd
    voter.sd = sd
    voter.cn_levy = cn_levy
    voter.wilm = wilm
    voter.code_home_city = code_home_city
    voter.sch_dist = sch_dist
    voter.party = party
    voter.date_reg = date_reg
    voter.pp_hist_1 = pp_hist_1
    voter.pp_hist_2 = pp_hist_2
    voter.pr_hist_1 = pr_hist_1
    voter.pr_hist_2 = pr_hist_2
    voter.pr_hist_3 = pr_hist_3
    voter.gen_hist_1 = gen_hist_1 
    voter.gen_hist_2 = gen_hist_2 
    voter.gen_hist_3 = gen_hist_3
    voter.gen_hist_4 = gen_hist_4
    voter.gen_hist_5 = gen_hist_5
    voter.sp_hist_1 = sp_hist_1
    voter.sp_hist_2 = sp_hist_2
    voter.sp_hist_3 = sp_hist_3
    voter.schl_hist_1 = schl_hist_1
    voter.schl_hist_2 = schl_hist_2
    voter.schl_hist_3 = schl_hist_3
    voter.schl_hist_4 = schl_hist_4
    voter.schl_hist_5 = schl_hist_5 
    voter.ref_hist_1 = ref_hist_1
    voter.ref_hist_2 = ref_hist_2
    voter.ref_hist_3 = ref_hist_3 
    voter.ref_hist_4 = ref_hist_4
    voter.ref_hist_5 = ref_hist_5
    voter.mail_no = mail_no
    voter.mail_apt = mail_apt
    voter.mail_street = mail_street
    voter.mail_city = mail_city
    voter.mail_state = mail_state
    voter.mail_zip = mail_zip
    voter.date_last_chg = date_last_chg 
    voter.code_change = code_change
    voter.status = status
    voter.gender = gender

    db.session.commit()
    return voter_schema.jsonify(voter)


# Run Server

if __name__ == '__main__':
    app.run(debug=True)
