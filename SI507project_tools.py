import csv
from flask import Flask, render_template, session, redirect, url_for
from model_classes_final import *


#################################################################################



@app.route('/')
def index():
    # conferences = Conference.query.all()
    # num_conferences = len(conferences)
    # x = Team.query.first()
    return render_template('index.html')



@app.route('/all_confs')
def see_confs():
    all_confs = []
    conferences = Conference.query.all()
    for c in conferences:
        all_confs.append((c.ConfName, c.NumSchools, c.G, c.W, c.L, c.Pct, c.Rk))
    return render_template('all_confs.html',all_confs=all_confs)



@app.route('/all_teams')
def see_teams():
    all_teams = []
    teams = Team.query.all()
    for t in teams:
        all_teams.append((t.school_name, t.conf_name, t.W, t.L, t.Pct, t.Rk, t.conf_id))
    return render_template('all_teams.html',all_teams=all_teams)



@app.route('/a_team/<team>')
def find_team(team):
    q = Team.query.filter_by(school_name=team).first()
    a_team = (q.school_name, q.conf_name, q.W, q.L, q.Pct, q.Rk, q.conf_id)
    return render_template('a_team.html',a_team=a_team)



@app.route('/a_conf/<conf>')
def find_conf(conf):
    q = Conference.query.filter_by(ConfName=conf).first()
    a_conf = (q.ConfName, q.NumSchools, q.G, q.W, q.L, q.Pct, q.Rk )
    return render_template('a_conf.html', a_conf=a_conf)



@app.route('/teams_in_conf/<conf>')
def teams_in_conf(conf):
    qc = Conference.query.filter_by(ConfName=conf).first()
    a_conf = ((qc.ConfName, qc.id))
    teams = Team.query.all()
    conf_teams = []
    for t in teams:
        if t.conf_id == qc.id:
            conf_teams.append((t.school_name, t.W, t.L, t.Pct, t.Rk))
    return render_template('teams_in_conf.html', conf_teams=conf_teams, conf_name = a_conf[0] )





############################################################################
## PUT THE POPULATING CODE BELOW HERE
############################################################################
"""I NEED TO CREATE TWO FUNCTIONS THAT RUN CODE TO POPULATE MY DB"""
## SOMETHING INTERESTING HAPPENED. I HAD THIS FOR LOOP BELOW THE __main__.
## THEN, I RAN THE CODE AND IT CREATED THE TABLES BUT NO INFO WAS SAVED INTO THE DB.
## WHILE THE PROGRAM WAS RUNNING I CUT/COPY THE CSV FILE LOOP ABOVE THE __main__ AND IT EXECUTED THE LOOP ONCE AND POPULATED THE DB SUCCESSFULLY.
def populate_conferences():
    with open('all_conf.csv', 'r', encoding='utf8') as csv_file:
        conf_lines = csv.reader(csv_file, delimiter=',')
        header = next(conf_lines, None)

        for cf in conf_lines:
            # print(cf)
            conf_inst = Conference(ConfName=cf[1], NumSchools=cf[2], G=cf[3], W=cf[4], L=cf[5], Pct=cf[6], Rk=cf[0])
            session.add(conf_inst)
            session.commit()
## BEFORE WHEN THIS CHUNK OF CODE WAS IN THE MODELS FILE. IT WOULD POPULATE THE DB TWICE EVERYTIME I RAN THE THE FLAS APP.
## I THINK I NEED TO FIND A WAY TO EXECUTE THE CSV WITHIN A FUNCTION.


def populate_teams():
    with open('overall_ranks.csv', 'r', encoding='utf8') as csv_file:
        team_lines = csv.reader(csv_file, delimiter=',')
        header = next(team_lines, None)

        for t in team_lines:
            q_conf = Conference.query.filter_by(ConfName=t[2]).first()
            a_conf_id = q_conf.id
            team_inst = Team(school_name=t[1], conf_name=t[2], conf_id=a_conf_id,  W=t[4], L=t[5], Pct=t[6], Rk=t[0])
            session.add(team_inst)
            session.commit()


# conf_id = session.query(Conference.Id).filter(Conference.ConfName.like(conf_var))

#################################################################################

if __name__ == '__main__':
    db.drop_all()
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    populate_conferences()
    populate_teams()
    app.run() # run with this: python main_app.py runserver


#################################################################################
