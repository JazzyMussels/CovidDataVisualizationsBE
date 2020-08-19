from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import csv 

# this function converts the csv data into json data to send to the front end
# using the csv module to convert to a dictionary
def make_json(path, index_name): 
    results = {} 
    #encoded with utf-8 as it supports many languages/mixtures of languages
    # and creates uniform encoding for all pages 
    with open('./csv_data/' + path, encoding='utf-8') as data: 
        info = csv.DictReader(data) 
        for rows in info: 
            key = rows[index_name] 
            results[key] = rows 
    return results

app = Flask(__name__)

#setting up support for the resources to be accessed from an outside domain
CORS(app, support_credentials=True)

# here are the various routes served up with the appropriate csv data
# each index is specified for easier access to the right information
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

@app.route('/borough_age')
def borough_age():
    return make_json('boroughs-by-age.csv', 'group')

@app.route('/borough_race')
def borough_race():
    return make_json('boroughs-by-race.csv', 'group')

@app.route('/borough_sex')
def borough_sex():
    return make_json('boroughs-by-sex.csv', 'group')

@app.route('/borough_timelines')
def borough_timelines():
    return make_json('boroughs-case-hosp-death.csv', 'DATE_OF_INTEREST')

app.run(port=3001)



