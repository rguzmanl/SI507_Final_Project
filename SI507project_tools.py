
import requests, json, csv
from flask import Flask
from data_scraping import *
import random
from random import sample





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


#############################################################


## FLASK ROUTES HERE:
## I STILL NEED TO DEFINE WHAT EXACTLY I WANT TO DISPLAY AND IF THERE WILL BE ANY KIND OF USER INTERACTION.
#############################################################
app = Flask(__name__)

## WELCOME PAGE
@app.route('/')
def home():
    return '<h1>Welcome to the College Foot Ball 2018 Statistics</h1>'


## ALL CONFERENCES (11 CONFERENCES) AND STATS PER CONFERENCE.
@app_route('/all_conferences')
def all_confs():
    "RETRIEVE ALL DATA CORRESPONING TO CONFERENCES FROM data_scraping.py"
    'list_of_rows = []'
    return 'TABLE FOR ALL CONFERENCES = all_conf.csv'


## ALL TEAMS (130 TEAMS) AND STATS PER TEAM.
@app_route('/all_teams')
def all_teams():
    "RETRIEVE ALL DATA CORRESPONING TO TEAMS FROM data_scraping.py"
    'final_rows = []'
    return 'TABLE FOR ALL CONFERENCES = overall_ranks.csv'


## ONE TEAM, MAY BE WITH USER INPUT BUT IT'LL NEED EXACT SPELLING I GUESS.
@app_route('/which_team/<team>')
def a_team():
    "WILL RETRIEVE A TEAM FROM data_scraping.py"
    'final_rows = []'
    return 'ONE PAGE WITH DATA FOR ONE SPECIFIC TEAM'


## ONE CONFERENCE, MAY BE WITH USER INPUT BUT IT'LL NEED EXACT SPELLING I GUESS.
@app_route('/which_conf/<conf>')
def a_conf():
    "WILL RETRIEVE A TEAM FROM data_scraping.py"
    'list_of_rows = []'
    return 'ONE PAGE WITH DATA FOR ONE SPECIFIC CONFERENCE'


## A ROUTE THAT SHOWS ONLY THE ASSOCIATED PRESS TOP 25 RANKED TEAMS.
@app_route('/which_conf/<conf>')
def top_25():
    "WILL SORT DATA USING THE AP_RANKS FROM data_scraping.csv"
    'final_rows = []'
    return 'ONE PAGE WITH A TABLE FOR THE TOP 25'


## AFTER THIS I'D LIKE TO USE plotly or matplotlib TO GENERATE SOME GRAPHS FROM OF THE DATA
## I WILL ADD AT LEAST ONE MORE ROUTE WITH THE GRAPH
#############################################################
@app.route('/graphs_top_25'):
def graph():
    return 'SOME GRAPH'






###
