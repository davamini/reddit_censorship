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
import ast

scope = [
    
    "https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"

    ]



def is_subreddit_recorded(subreddit):
	creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
	client = gspread.authorize(creds)
	sheet1 = client.open('subreddit_data').sheet1
	sheet2 = client.open('subreddit_data').get_worksheet(1)
	yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
	todays_date = str(datetime.date.today())
	try:
		location = get_coordinates(subreddit)
		date_of_last_upload = sheet2.cell(location[0], location[1] + 2).value

		if date_of_last_upload == yesterday:
			return True
	except:
		return False
	

def update_sheet2(coordinates, content):
	assert isinstance(content, str)

	creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
	client = gspread.authorize(creds)
	sheet1 = client.open('subreddit_data').sheet1
	sheet2 = client.open('subreddit_data').get_worksheet(1)

	sheet2.update_cell(coordinates[0], coordinates[1] + 1, content)

def is_comment_to_date(comment):
	comments_date = datetime.datetime.fromtimestamp(comment.created_utc).date()
	todays_date = datetime.date.today()
	if comments_date == todays_date:
		return True
	return False

def get_coordinates(subreddit):
	creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
	client = gspread.authorize(creds)
	sheet1 = client.open('subreddit_data').sheet1
	sheet2 = client.open('subreddit_data').get_worksheet(1)
	yesterday = datetime.date.today() - datetime.timedelta(days=1)
	todays_date = datetime.date.today()

	coordinates = (sheet2.find(subreddit).row, sheet2.find(subreddit).col)
	return coordinates

def get_subreddit_mod_dict(subreddit):
	"""Gets subreddit mod_dict from sheet2
	if already recorded
	"""
	creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
	client = gspread.authorize(creds)
	sheet1 = client.open('subreddit_data').sheet1
	sheet2 = client.open('subreddit_data').get_worksheet(1)

	coordinates = (sheet2.find(subreddit).row, sheet2.find(subreddit).col)

	mod_dict = sheet2.cell(coordinates[0], coordinates[1] + 1).value

	return ast.literal_eval(mod_dict)

def insert_to_sheet2(subreddit, mods):
	creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
	client = gspread.authorize(creds)
	sheet1 = client.open('subreddit_data').sheet1
	sheet2 = client.open('subreddit_data').get_worksheet(1)
	todays_date = datetime.date.today()

	insert_row = [subreddit, str(mods), str(todays_date)]
	sheet2.insert_row(insert_row, 2)




