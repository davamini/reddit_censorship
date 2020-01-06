import praw
import datetime
import sqlite3
import schedule
import time
from bs4 import BeautifulSoup
import requests as rq
import gsheets_funcs
import censorship_score_funcs
import ast

class Subreddit:

    def __init__(self, name):
        self.name = name
        self.mod_objects = Subreddit.get_moderators(self)
        self.score = Subreddit.censorship_score(self, self.mod_objects)
        self.mods = [mod.name for mod in Subreddit.get_moderators(self)]

    def get_moderators(self):
        """Gets the moderators' usernames
        from a given subreddit.
        """
        mods = []
        for moderator in reddit.subreddit(self.name).moderator():
            mods.append(moderator)
        return mods


    def censorship_score(self, moderators):
        """Returns a censorship score for the subreddit
        based on the removal rate of the given
        moderators. 
        """
        subscriber_count = reddit.subreddit(self.name).subscribers
        removal_count = 0

        if gsheets_funcs.is_subreddit_recorded(self.name):

            mods = censorship_score_funcs.get_mod_removal_count_dict_recorded(self.name, moderators)
            sheets_mods = gsheets_funcs.get_subreddit_mod_dict(self.name)

            for mod_name in mods.keys():
                sheets_mods[mod_name] += mods[mod_name]

            coordinates = gsheets_funcs.get_coordinates(self.name)
            gsheets_funcs.update_sheet2(coordinates, str(sheets_mods))

            for removals in sheets_mods.values():
                removal_count += removals

            score = (removal_count/subscriber_count)*100

            return score

        else:
            mods = censorship_score_funcs.get_mod_removal_count_dict_not_recorded(self.name, moderators)

            for removals in mods.values():
                removal_count += removals

            gsheets_funcs.insert_to_sheet2(self.name, mods)
            score = (removal_count/subscriber_count)*100

            return score

    def __str__(self):
        return 'Subreddit: {}\nScore {}\nModerators: {}'.format(self.name, self.score, self.mods)
