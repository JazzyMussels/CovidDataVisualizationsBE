# NYC Covid-19 Data Visualization Back End

This is a Flask application used to hold csv data and provide API endpoints for a data visualization project related to Covid 19 results in
New York City. The data was obtained from the 
New York City [Health Department](https://github.com/nychealth/coronavirus-data).

## Technologies Used
* Flask
* Python's unittest, csv, jsonify, and flask_cors modules

## Requirements
* [Python 3](https://www.python.org/downloads/)
* [Pip 3](https://pip.pypa.io/en/stable/installing/)

## Instructions
After cloning down the repo:
* run pip3 install flask
* run pip3 install flask_cors
* run python3 app.py

## Deployment
The resources contained here are also deployed through [Zappa](https://github.com/Miserlou/Zappa), 
which provides server-less web hosting for Python based applications through AWS Lambda and API Gateway. 
You can access the resources by starting [here](https://yibuf5tkd1.execute-api.us-east-1.amazonaws.com/dev/age_groups).
Each of the routes listed in app.py can be substituted to see the various json data.
