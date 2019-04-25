import os
import csv
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this


# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./cfb_data.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy


################################################################################

################################################################################

## CREATE CONFERENCE TABLE
## A CONFERENCE HAS MANY TEAMS.

class Conference(db.Model):
    __tablename__ = "conferences"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ConfName = db.Column(db.String(64)) #SHOULD I INCLUDE unique=True ???
    NumSchools = db.Column(db.Integer)
    G = db.Column(db.Integer)
    W = db.Column(db.Integer)
    L = db.Column(db.Integer)
    Pct = db.Column(db.Integer)
    Rk = db.Column(db.Integer)

    teams = db.relationship('Team',backref='Conference')

    def __repr__(self):
        return "Return string for conference {} (ID: {})".format(self.ConfName,self.id)



## CREATE CONFERENCE TABLE
## A TEAM HAS ONLY ONE CONFERENCE.

class Team(db.Model):
    # __tablename__ = "conferences"
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(64)) #SHOULD I INCLUDE unique=True ???
    conf_name = db.Column(db.String(64)) #SHOULD I INCLUDE unique=True ???
    conf_id = db.Column(db.Integer, db.ForeignKey("conferences.id"))
    W = db.Column(db.Integer)
    L = db.Column(db.Integer)
    Pct = db.Column(db.Integer)
    Rk = db.Column(db.Integer)


    def __repr__(self):
        return "Return string for team {} (ID: {})".format(self.school_name,self.id)



################################################################################

################################################################################


# , {{t[2]}}, {{t[4]}}, {{t[5]}}, {{t[6]}}, {{t[7]}}
