import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import datetime
import time
import reddit_censorship_base
from subreddits import subreddits

scope = [
    
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"

    ]


def scan_reddit_censorship():
    """Scans given subreddits
    on reddit.com for their censorship
    scores. Adds them to google sheets.
    """
    print('\nRunning RC Analysis...\n')
    for subreddit in subreddits:
        entry = subreddits.index(subreddit) + 2
        for i in range(3):
            try:
                for key, value in subreddit.items():
                    name = key
                    catagory = value
                print('In progress: {}'.format(name))
                today_date = datetime.date.today()
                new_subreddit = reddit_censorship_base.Subreddit(name)
                
                creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
                client = gspread.authorize(creds)
                sheet = client.open('subreddit_data').sheet1
                insert_row = [name, new_subreddit.score, catagory, str(today_date)]
                sheet.insert_row(insert_row, entry)
                print('Success with {} at {}\n'.format(name, datetime.datetime.now().time()))
                break
                
            except Exception as e:
                print('ERROR with {} subreddit at {}\n'.format(name, datetime.datetime.now().time()))
                print(str(e))
                time.sleep(300)
