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

def create_reddit_db():
    """Creates indexes.db
    for subreddit censorship indexes
    """
    conn = sqlite3.connect('rc.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE rc (subreddit text, mod_dict text, date date)""")

def db_insert(subreddit):
    """Inserts latest censorship indexes into
    reddit D
    """
    date_update = datetime.date.today()
    conn = sqlite3.connect('rc.db')
    c = conn.cursor()
    c.execute("INSERT INTO rc VALUES (:subreddit, :mod_dict, :date)",\
    {'subreddit': subreddit.name, 'mod_dict': str(subreddit.mod_dict), 'date': date_update})
    conn.commit()
    conn.close()
