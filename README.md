# SI-507 Final Project

### Roberto Guzmán

# 2018 Season College Football Rankings

## Description.
My project is a basic Flask web application that displays two tables, one with all the conferences in college football and their statistics, and one with the overall rankings of each team in the Football Bowl Subdivision (FBS). With the data collected I will create a Top 25 data base which I will also display. I will attempt to display some more routes, data per team, data per conference and a web page with graphics.



## What's in the project folder?
These are the files that I have used/created so far.

- ** advanced_expiry_caching.py
  - Borrowed from Project 4. Caches scraped data from a website.
- ** data_scraping.py
  - I created this file to handle the scraping process.
- ** SI507project_tools.py
  - It contains some of the main requirements of the project. Flask routes and Class definitions.
- ** SI507project_tests.py
  - It contains basic tests for some of the things I already have. More specifically, it tests the creation of class instances and the number of items in the conferences and teams lists.
- ** all_conf.csv
  - File created from data_scraping.py. All conferences.
- ** overall_ranks.csv
  - File created from data_scraping.py. All teams.
- ** all_teams.csv
  - File created from data_scraping.py. This is a third file I created but not very likely I will use it.
- ** cfb_cache.json
  - Cached data from the website.
- ** README.md
- ** data_base_diagram.PNG
  - The intended data base tables I will create.


## How does the program work?
### First part.
It scrapes data from https://www.sports-reference.com/ which I is cached in a JSON file, and then saves the data of interest in separate CSV files.

### Second part.
I will create classes of Team and Conference that I will use to display data about those instances. And to create web pages with the full data for all conferences and all teams.

### Third part.
I will generate graphics for the Top 25 teams and present them in a web application.




## How to run the program?
1. Make sure the files advanced_expiry_caching.py and data_scraping.py are in the same folder.
2. From Git Bash run: python data_scraping.py. This will create a JSON file with all the data scraped from the web three CSV files.
3. Run SI507project_tests.py to execute the tasks in SI507project_tools.py and test whether they pass the test.
4.













##
