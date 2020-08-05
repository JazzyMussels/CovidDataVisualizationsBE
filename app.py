from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import csv 

def make_json(path, index_name): 
    results = {} 
    with open('./csv_data/' + path, encoding='utf-8') as data: 
        info = csv.DictReader(data) 
        for rows in info: 
            key = rows[index_name] 
            results[key] = rows 
    return results

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/age_groups')
def ages():
    return make_json('by-age.csv', 'AGE_GROUP')

@app.route('/boroughs')
def boroughs():
    return make_json('by-boro.csv', 'BOROUGH_GROUP')

@app.route('/poverty_groups')
def poverty():
    return make_json('by-poverty.csv', 'POVERTY_GROUP')

@app.route('/race_groups')
def race():
    return make_json('by-race.csv', 'RACE_GROUP')

@app.route('/sex_groups')
def sex():
    return make_json('by-sex.csv', 'SEX_GROUP')

@app.route('/timeline')
def timelines():
    return make_json('case-hosp-death.csv', 'DATE_OF_INTEREST')

@app.route('/neighborhoods')
def neighborhood():
    return make_json('data-by-modzcta.csv', 'MODIFIED_ZCTA')

@app.route('/tests')
def testing():
    return make_json('tests.csv', 'DATE')



app.run(port=3001)


# get info for a specific date by typing it in


# NYC_CASE_COUNT	222522
# NYC_HOSPITALIZED_COUNT	56365
# NYC_CONFIRMED_DEATH_COUNT	18927

