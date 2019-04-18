from SI507project_tools import *
from data_scraping import *
import unittest
import csv, json, requests
import numpy as np
import random
import itertools


#####################################################################################

print('\n')



## TESTS FOR TEAM AND CONFERENCE INSTANCES.
#####################################################################################

class anInstance(unittest.TestCase):

    def test_class_team(self):
        self.team = a_team
        self.assertIsInstance(self.team, Team, "Testing if an instance of Team was created")

    def test_class_conference(self):
        self.conf = a_conf
        self.assertIsInstance(self.conf, Conference, "Testing if an instance of Conference was created")



## TESTS TO COUNT THE NUMBER OF TEAMS AND CONFERENCES PER TABLE.
#####################################################################################

class NumberRows(unittest.TestCase):

    def test_num_teams(self):
        self.num_teams = len(final_rows)
        self.assertEqual(self.num_teams, 130, 'Testing if number of teams is 130')
        # print(self.num_teams)

    def test_num_conferences(self):
        self.num_confs = len(list_of_rows)
        self.assertEqual(self.num_confs, 11, 'Testing if number of conferences is 11')
        # print(self.num_confs)











##############
if __name__ == "__main__":
    unittest.main(verbosity=2)
