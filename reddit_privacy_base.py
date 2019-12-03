import pandas as pd
import praw
import datetime
import sqlite3
import schedule

reddit = praw.Reddit(client_id='epKPUwrZ5yb51g',
                     client_secret="iwkv2-KQ3-VduKJDdca57vls35w", password='3De1OlR#',
                     user_agent='ardonpage', username='ardonpage')


subreddits = [
        
        'HongKong', 'Sino', 'UCSD', 'Conservative', 'Libertarian', 
        'socialism', 'communism', 'VoteBlue', 'history', 'AskReddit', 
        'JoeRogan', 'nba', 'Tinder', 'nottheonion', 'NoStupidQuestions',
        'DeathStranding', 'China', 'Jokes', 'liberalgunowners', 'changemyview', 
        'HolUp'

        ]



class Subreddit:

    def __init__(self, name):
        self.name = name
        self.mod_objects = Subreddit.get_moderators(self)
        self.score = Subreddit.moderator_censor_index(self, self.mod_objects)
        self.mods = [mod.name for mod in Subreddit.get_moderators(self)]

    def get_moderators(self):
        """Gets the moderators' usernames
        from a given subreddit.
        """
        mods = []
        for moderator in reddit.subreddit(self.name).moderator():
            mods.append(moderator)
        return mods


    def moderator_censor_index(self, moderators):
        """Returns a censorship score for the subreddit
        based on the removal rate of the given
        moderators. 
        """
        subscriber_count = reddit.subreddit(self.name).subscribers
        removal_count = 0
        mods = {}
        mod_removal_count = 0
        for moderator in moderators:
            for comment in moderator.comments.new(limit = 500):
                if 'removed' in comment.body:
                    removal_count += 1
                    mod_removal_count += 1
            mods[moderator.name] = mod_removal_count
            mod_removal_count = 0
        #print(mods)
        score = (removal_count*(subscriber_count/(len(moderators)*20)))/subscriber_count
        return score

    def __str__(self):
        return 'Subreddit: {}\nScore {}\nModerators: {}'.format(self.name, self.score, self.mods)



def create_reddit_db():

    conn = sqlite3.connect('indexes.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE reddit_indexes (subreddit text, indexes integer, date date)""")

def db_insert(subreddit, new_index):
        date_update = datetime.datetime.today()
        conn = sqlite3.connect('indexes.db')
        c = conn.cursor()
        c.execute("INSERT INTO reddit_indexes VALUES (:subreddit, :indexes, :date)",\
        {'subreddit': subreddit, 'indexes': new_index, 'date': date_update})
        conn.commit()
        conn.close()

for subreddit in subreddits:
    for i in range(3):
        try:
            occurance = datetime.datetime.today()
            new_subreddit = Subreddit(subreddit)
            db_insert(new_subreddit.name, new_subreddit.score)
            print('Success with {} at {}\n'.format(subreddit, occurance))
            break
        except:
            print('ERROR with {} subreddit at {}\n'.format(subreddit, occurance))
