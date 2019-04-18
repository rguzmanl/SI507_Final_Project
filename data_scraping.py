# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests, json, csv
from advanced_expiry_caching import Cache



###########################################################################################################
## CACHING DATA

FILENAME = "cfb_cache.json"
URL = "https://www.sports-reference.com/cfb/years/2018.html"
URL_into_conf = "https://www.sports-reference.com" # THIS URL WILL BE USED TO CONCATENATE WITH THE href OF EACH CONFERENCE.
URL_overall = "https://www.sports-reference.com/cfb/years/2018-ratings.html"

PROGRAM_CACHE = Cache(FILENAME) # create a cache -- stored in a file of this name

## THIS FUNCTION CHECKS FOR DATA IN THE CACHE FILE OR EXECUTES THE REQUEST TO THE WEB PAGE WHEN THE CHACE FILE IS EMPTY
def access_page_data(url):
    data = PROGRAM_CACHE.get(url) # .get() METHOD IS IMPORTED FROM advanced_expiry_caching IT GENERATES THE UNIQUE IDENTIFIER.
    if not data:
        data = requests.get(url).text # .get() THIS METHOD IS FROM BS4.
        # print(data)
        PROGRAM_CACHE.set(url, data) # default here with the Cache.set tool is that it will expire in 7 days, which is probs fine, but something to explore
    return data

###########################################################################################################
## MAKING FIRST REQUEST TO THE 2018 ALL CONFERENCES TABLE

all_conf = access_page_data(URL)
all_conf_soup = BeautifulSoup(all_conf, features="html.parser")
table_confs = all_conf_soup.find('div',{'id':"all_conferences"})
conf_table = table_confs.find_all('tbody')

# THE INDEX USED IN THE NEXT LINE IS TO SPECIFY TO WHICH TABLE WE'LL REFER TO IN THE WHOLE WEBPAGE (BECAUSE THERE ARE MORE TABLES AND WE ARE INTERESTED IN THE FIRST ONE).
find_tr = conf_table[0].find_all('tr')

with open('all_conf.csv', 'w', newline = '') as csv_file:
    row_input = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    row_input.writerow(['Rk','Conference', 'Schs', 'G', 'W', 'L', 'Pct','Bowls G', 'Bowls W', 'Bowls L', 'Bowl Pct', 'SRS', 'SOS', 'Pre', 'Final', 'Champion'])

    # REFERENCE CODE: https://stackoverflow.com/questions/46242664/python-web-scraping-html-table-and-printing-to-csv
    list_of_rows = []
    for row in find_tr:
        list_of_cells = []
        for cell in row.find_all(["th","td"]):
            text = cell.get_text()
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)

    for cell in list_of_rows:
        rk = cell[0]
        conf = cell[1]
        schs = cell[2]
        games = cell[3]
        wins = cell[4]
        loss = cell[5]
        pct = cell[6]
        b_games = cell[7]
        b_wins = cell[8]
        b_loss = cell[9]
        b_pct = cell[10]
        srs = cell[11]
        sos = cell[12]
        pre = cell[13]
        final = cell[14]
        champion = cell[15]

        row_input.writerow([rk, conf, schs, games, wins, loss, pct, b_games, b_wins, b_loss, b_pct, srs, sos, pre, final, champion])

## UP TO THIS POINT MY CODE CREATES THE FIRST TABLE "ALL CONFERENCES"
###########################################################################################################


###########################################################################################################
## MAKING REQUESTS TO EACH CONFERENCE LINK
# I WILL KEEP THIS CODE IN CASE THERE IS AN EASY WAY TO RETRIEVE DATA PER CONFERNCE TABLE

## GIVES ME THE LINK PER CONFERENCE
conf_links = table_confs.find_all('a')


links_to_confs = []
for each_conf in conf_links:
    conf_url = URL_into_conf + each_conf['href']
    links_to_confs.append(conf_url)

per_conf_list = []
for c_link in links_to_confs:

    access_to_conf = access_page_data(c_link)
    conf_soup = BeautifulSoup(access_to_conf, features="html.parser")
    per_conf = conf_soup.find('div',{'id':"all_standings"})
    per_conf_table = per_conf.find_all('tbody')
    conf_tr = per_conf_table[0].find_all('tr')
    per_conf_list.append(conf_tr)

with open('all_teams.csv', 'w', newline = '') as csv_file:
    row_input = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    row_input.writerow(['East','W', 'L', 'Pct', 'W', 'L', 'Pct','Off', 'Def', 'SRS','SOS', 'Rk AP Curr', 'Rk AP Pre', 'Rk AP High', 'Notes'])

    all_teams = []
    for t_row in per_conf_list:
        for t in t_row:
            lst_of_teams_conf =[]
            for d_conf in t.find_all(["th","td"]):
                text_conf = d_conf.get_text()
                lst_of_teams_conf.append(text_conf)
            if lst_of_teams_conf[1] != 'W':
                all_teams.append(lst_of_teams_conf)

    ####################################
    # I WILL NOT USE THESE DATA PROBABLY
    ####################################
    for l in all_teams:

        zone = l[0]
        ov_wins = l[1]
        ov_loss = l[2]
        ov_pct = l[3]
        cf_wins = l[4]
        cf_loss = l[5]
        cf_pct = l[6]
        pt_game_off = l[7]
        pt_game_def = l[8]
        srs = l[9]
        sos = l[10]
        ap_curr = l[11]
        ap_pre = l[12]
        ap_high = l[13]
        notes = l[14]

        row_input.writerow([zone, ov_wins, ov_loss, ov_pct, cf_wins, cf_loss, cf_pct, pt_game_off, pt_game_def, srs, sos, ap_curr, ap_pre, ap_high, notes])

# AT THIS POINT I HAVE EACH CONFERENCE AS AN ELEMENT IN A per_conf_list OF BS OBJECTS.
# I THINK I NEED TO DEFINE A FUNCTION SO I CAN CREATE DIFFERENT CSV FILES PER CONFERENCE TABLE.
# def create_a_csv_file():


###########################################################################################################

# MY NEXT STEP IS TO RETRIEVE THE OVERALL DATA/RANKS AND STATS FROM:
# https://www.sports-reference.com/cfb/years/2018-ratings.html
# AND MAY BE USE THAT DATA INSTEAD OF THE CHUNK OF CODE ABOVE

###########################################################################################################

# IN THE FOLLOWING CHUNK OF CODE I'LL GET THE DATA FROM THE OVERALL RANKINGS

overall_conf = access_page_data(URL_overall)
overall_conf_soup = BeautifulSoup(overall_conf, features="html.parser")
table_overall = overall_conf_soup.find('div',{'id':"all_ratings"})
overall_table = table_overall.find_all('tbody')
find_tr_overall = overall_table[0].find_all('tr')


with open('overall_ranks.csv', 'w', newline = '') as csv_file:
    row_input = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    row_input.writerow(['Rk','School', 'Conf', 'AP Rank', 'W', 'L', 'OSRS','DSRS', 'SRS', 'Score Off', 'Score Deff', 'Pass Off', 'Pass Def', 'Rush Off', 'Rush Def', 'Tot Off', 'Tot Def'])


    final_rows = []
    valid_rows = []
    rows_teams = []

    ## ALL THESE CRAZY FOR LOOPS JUST TO CLEANED UNDESIRED DATA.
    ## THERE WERE SOME HIDDEN HTML ELEMENTS THAT CAUSED A LOT OF TROUBLE
    for team_row in find_tr_overall:

        team_cells = []
        for data in team_row.find_all(['th','td']):
            cell_data = data.get_text()
            team_cells.append(cell_data)
        rows_teams.append(team_cells)

    for t in rows_teams:
        if t[0] != 'Rk':
            valid_rows.append(t)

    for e in valid_rows:
        if e[0] != '':
            final_rows.append(e)


    # print(len(final_rows))
    for all in final_rows:

        rk = all[0]
        sch = all[1]
        conf = all[2]
        ap_rank = all[3]
        wins = all[4]
        loss = all[5]
        osrs = all[6]
        dsrs = all[7]
        srs = all[8]
        sc_off = all[9]
        sc_def = all[10]
        pass_off = all[11]
        pass_def = all[12]
        rush_off = all[13]
        rush_def = all[14]
        tot_off = all[15]
        tot_def = all[16]

        row_input.writerow([rk, sch, conf, ap_rank, wins, loss, osrs, dsrs, srs, sc_off, sc_def, pass_off, pass_def, rush_off, rush_def, tot_off, tot_def])



##############################


print('\n')
###
