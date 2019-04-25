from SI507project_tools import *
from data_scraping import *
import unittest
import csv, json, requests
import random
import itertools
from flask import Flask, render_template, session, redirect, url_for
from model_classes_final import *
from flask_sqlalchemy import SQLAlchemy

# from flask_testing import TestCase
# from flask_routes import create_app, db
# create_app, db
#####################################################################################





## TESTS TO CONFIRM WE HAVE THE CORRECT NUMBER OF TEAMS AND CONFERENCES PER TABLE.
## THIS TEST IS IMPORTING TWO VARIABLES FROM data_scraping.py
## TESTS TO DETERMINE WHETHER THERE IS DATA IN THE CACHE FILE.
#####################################################################################


class CachedData(unittest.TestCase):

    def test_cached_data(self):
        if not data:
            self.data = True, 'There is data in the CACHE file.'


class CreatingCSV(unittest.TestCase):

    def test_num_teams(self):
        self.num_teams = len(final_rows)
        self.assertEqual(self.num_teams, 130, 'Testing if number of teams is 130')
        # print(self.num_teams)

    def test_num_conferences(self):
        self.num_confs = len(list_of_rows)
        self.assertEqual(self.num_confs, 11, 'Testing if number of conferences is 11')
        # print(self.num_confs)

    def test_conf_translation(self):
        if all[2] in confs_dict.keys():
            self.conf = confs_dict[all[2]]
        self.assertEqual(self.conf, confs_dict[all[2]], 'Testing whether translation of conferences was successful')



## TESTS FOR FLASK
## https://stackoverflow.com/questions/17791571/testing-flask-sql-alchemy
## https://pythonhosted.org/Flask-Testing/
#####################################################################################



    # SQLALCHEMY_DATABASE_URI = 'sqlite:///./TEST_cfb_data.db'
    # TESTING = True
    #
    # def create_app(self):
    #
    #     # pass in test configuration
    #     app = Flask(__name__)
    #     app.config['TESTING'] = True
    #     return create_app(self)
    #
    # def setUp(self):
    #
    #     db.create_all()
    #
    # def tearDown(self):
    #
    #     db.session.remove()
    #     db.drop_all()









#####################################################################################
if __name__ == "__main__":
    unittest.main(verbosity=2)




## NOT NEEDED
## TESTS FOR TEAM AND CONFERENCE INSTANCES.
#####################################################################################

class anInstance(unittest.TestCase):

    def test_class_team(self):
        self.team = a_team
        self.assertIsInstance(self.team, Team, "Testing if an instance of Team was created")

    def test_class_conference(self):
        self.conf = a_conf
        self.assertIsInstance(self.conf, Conference, "Testing if an instance of Conference was created")


### NOT USED ###
### THIS CODE WAS ORIGINALLY IN SI507project_tools.py

## TESTS TO CREATE INSTANCES OF CLASSES "Team" and "Conference"
## WITH THESE I CAN CREATE TWO ROUTES WITH ALL DATA PER CLASS.
##############################################################

class Team:

    # I think instead of just a name ('str') as argument, I will enter a list ('row') whose items will be the data cells for each team. From there I will pick some specific cells to form an instance of Team.
    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        # add more instances variables

    def __str__(self):
        return "{} is an instance of the class Team and it is in conference {}".format(self.name, self.conf)


a_team = Team('"Michigan"', '"Big 10"')
# print(a_team)
# print(type(a_team))



class Conference:

    def __init__(self, name):
        self.name = name
        # add more instances variables

    def __str__(self):
        return "{} is an instance of the class Conference".format(self.name)

a_conf = Conference('"Big 10"')
# print(a_conf)
