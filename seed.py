from .models import Voter
import json
from app import db

with open('data.json', 'r') as data:
    json_object = json.load(data)
    for entry in json_object['voters']:
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
