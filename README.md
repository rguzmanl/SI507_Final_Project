# SI-507 Final Project

### Roberto Guzmán

# 2018 Season College Football Rankings

## Description.
My project is a Flask web application that relies on two main tables, whose relationship is one-to-many.
One table has a list of all the conferences (and stats) in College Football (Division I). The other one has all the teams and stats.
My application consists of six routes that display the two whole tables and combinations of specific information.



## What's in the project folder?
These are the files that I have used/created so far.

- **advanced_expiry_caching.py**
  - Borrowed from Project 4. Caches scraped data from a website.
- **data_scraping.py**
  - I created this file to handle the scraping process.
- **model_classes_final.py**
  - This file contains the Class definitions that the represent the tables in the database.
- **SI507project_tools.py**
  - It contains some of the main requirements of the project. Flask routes and code to populate the database.
- **SI507project_tests.py**
  - It contains basic tests for some of the things I already have. It runs very basic tests. For example, verifies that the CSV files created have the correct amount of information, it tests whether the CACHE file has data, and it also tests a dictionary that handles a conferences names translations needed to manipulate some data.
- **all_conf.csv**
  - File created from data_scraping.py. All conferences.
- **overall_ranks.csv**
  - File created from data_scraping.py. All teams. *In this file I added a Percentage column whose value was calculated within the code*
- **all_teams.csv**
  - File created from data_scraping.py. This is a third file I created but not very likely I will use it. *no longer needed*
- **cfb_cache.json**
  - Cached data from the website.
- **README.md**
- **data_base_diagram.PNG**
  - The intended data base tables I will create.
- **cfb_data.db**
  - This is the database created as a result of the execution of this program.
- **requirements.txt**
  - It contains all the information of the modules and libraries used in this project.
- **/templates**
  - This folder contains several html files that provide basic templating to the web pages.



## How does the program work?
### First part.
It scrapes data from https://www.sports-reference.com/ which I is cached in a JSON file, and then saves the data of interest in separate CSV files.

### Second part.
Using Flask-SQLAlchemy, this program generates the tables in the database and populates them.

### Third part.
By running the program, six different routes are generated, which display different levels of data in webpages.



## How to run the program.
1. Make sure all the files are in the same folder.
  - **NOTE:** For testing purposes you can/should delete (or save in a separate folder) the provided files: cfb_cache.json, all_conf.csv, all_teams.csv, and cfb_data.db. Which will be generated when the program is run.
2. From Git Bash run: python data_scraping.py. This will create a CACHED JSON file and from this file it will generate the two CSV files that will used to create the database later.
3. Run SI507project_tests.py to test whether the CACHE and CSV files were created correctly.
4. Run SI507project_tools.py to generate and populate the database. Also, this code will activate the Flask app that will allow us to present the data in the web browser.



## How to interact with the application.
1. When you run the program, you will see this http<i><i>://127.0.0.1:5000/. Copy/paste it into your browser to go to the home page.
2. The home page has a welcome message and a couple of buttons(links) to the two whole tables.
  - You can also go to the tables directly by typing this in your browser: http<i><i>://127.0.0.1:5000/all_teams, or http<i><i>://127.0.0.1:5000/all_confs
3. You can also retrieve either one single conference or team by typing this into your browser: http<i><i>://127.0.0.1:5000/a_team/<enter a team name here>, or http<i><i>://127.0.0.1:5000/a_conf/<enter a conference name here>
  - **NOTE: details about exact spelling of team and conferences below.**
4. The final option is to retrieve all the teams within a conference by typing this: http<i><i>://127.0.0.1:5000/teams_in_conf/<enter a conference name here>


## Examples of what to enter in the browser. You can just copy and paste this.

- http<i><i>://127.0.0.1:5000/a_team/Michigan
- http<i><i>://127.0.0.1:5000/a_conf/Big Ten Conference
- http<i><i>://127.0.0.1:5000/teams_in_conf/Big Ten Conference

## More options of teams and conferences names:

*There is no relationship necessarily between the teams and conferences in this table, it is just for you to copy and paste different names in order to avoid typos.*

http<i><i>://127.0.0.1:5000/a_team/<enter a team name here>
http<i><i>://127.0.0.1:5000/a_conf/<enter a conference name here>
http<i><i>://127.0.0.1:5000/teams_in_conf/<enter a conference name here>

|Conferences               |Teams              |
|--------------------------|:-----------------:|
|Big 12 Conference         |Texas              |
|Southeastern Conference   |Washington         |
|Atlantic Coast Conference |Colorado           |
|Independent               |UCLA               |
|Mountain West Conference  |Georgia Tech       |
|Mid-American Conference   |North Texas        |


## What you can expect to see

Homepage:
(https://github.com/rguzmanl/SI507_Final_Project/blob/master/result_imgs/home.png)




##
