import pandas as pd
import praw
import datetime
import sqlite3
import schedule
import time
from bs4 import BeautifulSoup
import requests as rq

content = rq.get('https://redditmetrics.com/top').content
soup = BeautifulSoup(content, 'lxml')

fields = soup.find_all("a")

lst = []
for field in fields:
    lst.append(field.text)

subreddits = []
for subreddit in lst:
    if '/r/' in subreddit:
        subreddits.append(subreddit.replace('/r/', ''))

reddit = praw.Reddit(client_id='epKPUwrZ5yb51g',
                     client_secret="iwkv2-KQ3-VduKJDdca57vls35w", password='3De1OlR#',
                     user_agent='ardonpage', username='ardonpage')


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
        length_mods = len(moderators)
        subscriber_count = reddit.subreddit(self.name).subscribers
        removal_count = 0
        mods = {}
        mod_removal_count = 0
        for moderator in moderators:
            for i in range(3):
                try:
                    for comment in moderator.comments.new(limit = 1000):
                        if 'removed' in comment.body:
                            mod_removal_count += 1
                    mods[moderator.name] = mod_removal_count
                    mod_removal_count = 0
                except:
                    print('Mod Error for {} in {}'.format(moderator, self.name))
                    break
        for removals in mods.values():
            removal_count += removals
        #print(mods)
        #print(removal_count)
        #print(reddit.subreddit(self.name).subscribers)
        score = (removal_count/subscriber_count)*100
        return score

    def __str__(self):
        return 'Subreddit: {}\nScore {}\nModerators: {}'.format(self.name, self.score, self.mods)



def create_reddit_db():
    """Creates indexes.db
    for subreddit censorship indexes
    """
    conn = sqlite3.connect('rc.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE reddit_indexes (subreddit text, scores integer, category text, date date)""")

def db_insert(subreddit, score, category):
    """Inserts latest censorship indexes into
    reddit D
    """
    date_update = datetime.date.today()
    conn = sqlite3.connect('rc.db')
    c = conn.cursor()
    c.execute("INSERT INTO rc VALUES (:subreddit, :score, :category, :date)",\
    {'subreddit': subreddit, 'score': score, 'category': category, 'date': date_update})
    conn.commit()
    conn.close()
