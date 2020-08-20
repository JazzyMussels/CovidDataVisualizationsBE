import unittest
import json
from app import app

# The following series of tests look for specific values 
# returned by categories in the json data of a given route
class BasicTestCase(unittest.TestCase):
    def test_ages(self):
        tester = app.test_client(self)
        response = tester.get('/age_groups', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['45-64']["DEATH_COUNT"], "4263")

    def test_boroughs(self):
        tester = app.test_client(self)
        response = tester.get('/boroughs', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['Bronx']['BOROUGH_GROUP'], "Bronx")

    def test_poverty(self):
        tester = app.test_client(self)
        response = tester.get('/poverty_groups', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["Very high poverty"]["HOSPITALIZED_RATE_ADJ"], "834.42")

    def test_race(self):
        tester = app.test_client(self)
        response = tester.get('/race_groups', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["Black/African-American"]['CASE_COUNT'], "35895")

    def test_sex(self):
        tester = app.test_client(self)
        response = tester.get('/sex_groups', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['Male']['DEATH_COUNT'], "11365")

    def test_timelines(self):
        tester = app.test_client(self)
        response = tester.get('/timeline', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['03/02/2020']['CASE_COUNT'], "0")

    def test_neighborhood(self):
        tester = app.test_client(self)
        response = tester.get('/neighborhoods', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['10010']['PERCENT_POSITIVE'], "4.1")

    def test_testing(self):
        tester = app.test_client(self)
        response = tester.get('/tests', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['03/23/2020']['TOTAL_TESTS'], "5973")

    def test_borough_age(self):
        tester = app.test_client(self)
        response = tester.get('/borough_age', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['75+']['MN_HOSPITALIZED_COUNT'], "2716")

    def test_borough_race(self):
        tester = app.test_client(self)
        response = tester.get('/borough_race', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['Asian/Pacific-Islander']['BK_HOSPITALIZED_RATE_ADJ'], "210.21")

    def test_borough_sex(self):
        tester = app.test_client(self)
        response = tester.get('/borough_sex', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['Boroughwide']['SI_DEATH_COUNT'], "897")

    


if __name__ == '__main__':
    unittest.main()

    # b"'Bronx': { 'BOROUGH_GROUP': 'Bronx', 'CASE_COUNT': '50044', 'CASE_RATE': '3494.37', 'DEATH_COUNT': '3934', 'DEATH_RATE': '274.7', 'HOSPITALIZED_COUNT': '12650', 'HOSPITALIZED_RATE': '883.3'}"