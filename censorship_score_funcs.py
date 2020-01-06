import praw
import datetime
import sqlite3
import schedule
import time
from bs4 import BeautifulSoup
import requests as rq
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import gsheets_funcs

def get_mod_removal_count_dict_recorded(subreddit, moderators):
    mods = {}

    for moderator in moderators:
        name = moderator.name
        if name == 'AutoModerator':
            continue

        mods[name] = 0
        try:
            for comment in moderator.comments.new(limit = 1000):
                if gsheets_funcs.is_comment_to_date(comment) == False:
                    break

                elif 'removed' in comment.body:
                    mods[name] += 1
        except:
            print('Mod Error for {} in {}'.format(moderator, subreddit))
            break

    return mods

def get_mod_removal_count_dict_not_recorded(subreddit, moderators):
    mods = {}

    for moderator in moderators:
        name = moderator.name
        if name == 'AutoModerator':
            continue

        mods[name] = 0
        try:
            for comment in moderator.comments.new(limit = 1000):
                if 'removed' in comment.body:
                    mods[name] += 1
        except:
            print('Mod Error for {} in {}'.format(moderator, subreddit))
            break

    return mods
    
