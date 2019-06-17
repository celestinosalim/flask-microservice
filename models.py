from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lnujflspcwrqms:565ca04b0f1bb7c7153eb44e8872e89172801ab9185cd99ace4dd7135f35c119@ec2-107-20-230-70.compute-1.amazonaws.com:5432/d56amubtoat4hh'
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Db
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Voter(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    voter_id = db.Column(db.String)
    last_name = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    mid_init = db.Column(db.String(1))
    suffix = db.Column(db.String(5))
    date_of_birth = db.Column(db.String)
    birth_year = db.Column(db.String)
    phone = db.Column(db.String)
    address = db.Column(db.String(200))
    home_no = db.Column(db.String(15))
    home_apt = db.Column(db.String(15))
    home_street = db.Column(db.String(200))
    home_dev = db.Column(db.String(200))
    home_city = db.Column(db.String(200))
    home_zipcode = db.Column(db.String(200))
    county = db.Column(db.String(200))
    ed = db.Column(db.String(15))
    rd = db.Column(db.String(15))
    sd = db.Column(db.String(15))
    cn_levy = db.Column(db.String(15))
    wilm = db.Column(db.String(15))
    code_home_city = db.Column(db.String(15))
    sch_dist = db.Column(db.String(15))
    party = db.Column(db.String(15))
    date_reg = db.Column(db.String(15))
    pp_hist_1 = db.Column(db.String(15))
    pp_hist_2 = db.Column(db.String(15))
    pr_hist_1 = db.Column(db.String(15))
    pr_hist_2 = db.Column(db.String(15))
    pr_hist_3 = db.Column(db.String(15))
    gen_hist_1 = db.Column(db.String(15))
    gen_hist_2 = db.Column(db.String(15))
    gen_hist_3 = db.Column(db.String(15))
    gen_hist_4 = db.Column(db.String(15))
    gen_hist_5 = db.Column(db.String(15))
    sp_hist_1 = db.Column(db.String(15))
    sp_hist_2 = db.Column(db.String(15))
    sp_hist_3 = db.Column(db.String(15))
    schl_hist_1 = db.Column(db.String(15))
    schl_hist_2 = db.Column(db.String(15))
    schl_hist_3 = db.Column(db.String(15))
    schl_hist_4 = db.Column(db.String(15))
    schl_hist_5 = db.Column(db.String(15))
    ref_hist_1 = db.Column(db.String(15))
    ref_hist_2 = db.Column(db.String(15))
    ref_hist_3 = db.Column(db.String(15))
    ref_hist_4 = db.Column(db.String(15))
    ref_hist_5 = db.Column(db.String(15))
    mail_no = db.Column(db.String(15))
    mail_apt = db.Column(db.String(15))
    mail_street = db.Column(db.String(100))
    mail_city = db.Column(db.String(100))
    mail_state = db.Column(db.String(100))
    mail_zip = db.Column(db.String(100))
    date_last_chg = db.Column(db.String(15))
    code_change = db.Column(db.String(100))
    status = db.Column(db.String(10))
    gender = db.Column(db.String(10))

    def __init__(self, voter_id, last_name, first_name, mid_init, suffix, date_of_birth, 
    birth_year, phone, address, home_no, home_apt, home_street,  home_dev,
    home_city, home_zipcode, county, ed, rd, sd, cn_levy, wilm, code_home_city, 
    sch_dist, party, date_reg, pp_hist_1, pp_hist_2, pr_hist_1, pr_hist_2,
    pr_hist_3, gen_hist_1, gen_hist_2, gen_hist_3, gen_hist_4, gen_hist_5,
    sp_hist_1, sp_hist_2, sp_hist_3, schl_hist_1, schl_hist_2, schl_hist_3,
    schl_hist_4, schl_hist_5, ref_hist_1, ref_hist_2, ref_hist_3, ref_hist_4,
    ref_hist_5, mail_no, mail_apt, mail_street, mail_city, mail_state, mail_zip,
    date_last_chg, code_change, status, gender):
            self.voter_id = voter_id,    
            self.last_name = last_name,
            self.first_name = first_name
            self.mid_init = mid_init
            self.suffix = suffix
            self.date_of_birth = date_of_birth
            self.birth_year = birth_year
            self.phone = phone
            self.address = address
            self.home_no = home_no
            self.home_apt = home_apt
            self.home_street = home_street
            self.home_dev = home_dev
            self.home_city = home_city
            self.home_zipcode = home_zipcode
            self.county = county
            self.ed = ed
            self.rd = rd
            self.sd = sd
            self.cn_levy = cn_levy
            self.wilm = wilm
            self.code_home_city = code_home_city
            self.sch_dist = sch_dist
            self.party = party
            self.date_reg = date_reg
            self.pp_hist_1 = pp_hist_1
            self.pp_hist_2 = pp_hist_2
            self.pr_hist_1 = pr_hist_1
            self.pr_hist_2 = pr_hist_2
            self.pr_hist_3 = pr_hist_3
            self.gen_hist_1 = gen_hist_1 
            self.gen_hist_2 = gen_hist_2 
            self.gen_hist_3 = gen_hist_3
            self.gen_hist_4 = gen_hist_4
            self.gen_hist_5 = gen_hist_5
            self.sp_hist_1 = sp_hist_1
            self.sp_hist_2 = sp_hist_2
            self.sp_hist_3 = sp_hist_3
            self.schl_hist_1 = schl_hist_1
            self.schl_hist_2 = schl_hist_2
            self.schl_hist_3 = schl_hist_3
            self.schl_hist_4 = schl_hist_4
            self.schl_hist_5 = schl_hist_5 
            self.ref_hist_1 = ref_hist_1
            self.ref_hist_2 = ref_hist_2
            self.ref_hist_3 = ref_hist_3 
            self.ref_hist_4 = ref_hist_4
            self.ref_hist_5 = ref_hist_5
            self.mail_no = mail_no
            self.mail_apt = mail_apt
            self.mail_street = mail_street
            self.mail_city = mail_city
            self.mail_state = mail_state
            self.mail_zip = mail_zip
            self.date_last_chg = date_last_chg 
            self.code_change = code_change
            self.status = status
            self.gender = gender
    
    