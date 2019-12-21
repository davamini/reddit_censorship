political_subreddits = [

			  	{'socialism': 'political'}, {'communism': 'political'},
			  	{'VoteBlue': 'political'}, {'liberalgunowners': 'political'},
			  	{'Libertarian': 'political'},{'Conservative': 'political'}, 
			  	{'Sino': 'political'}, 

			  	]

academic_subreddits = [
			  
			  	{'ucla': 'academic'}, {'ucsc': 'academic'},
			  	{'UCSD': 'academic'}, {'berkeley': 'academic'},
			  	{'ucr': 'academic'}, {'ucmerced': 'academic'},
			  	{'ucdavis': 'academic'}, {'uci': 'academic'},
			  	{'ucsantabarbara': 'academic'},

			  	]

news_subreddits = [
			  
			  	{'UpliftingNews': 'news'}, {'news': 'news'},
			  	{'TrueNews': 'news'}, {'TrueReddit': 'news'},
			  	]

gaming_subreddits = [
			  
			  	{'sekiro': 'gaming'}, {'DeathStranding': 'gaming'},
			  	{'gaming': 'gaming'}, {'leagueoflegends': 'gaming'},
			  	{'pathofexile': 'gaming'},

			  	]

geography_subreddits = [
			 
			  	{'HongKong': 'geography'}, {'europe': 'geography'}, 
			  	{'canada': 'geography'}, {'China': 'geography'},

			  	]

educational_subreddits = [
			 
			  	{'history': 'educational'}, {'YouShouldKnow': 'educational'},
			  	{'howto': 'educational'}, {'OutOfTheLoop': 'educational'},

			  	]

ask_subreddits = [
			 
			  	{'NoStupidQuestions': 'ask_'}, {'AskReddit': 'ask_'},
			  	{'TrueAskReddit': 'ask_'}, {'askhistorians': 'ask_'},

			  	]

humor_subreddits = [
			 
			  	{'Jokes': 'humor'}, {'humor': 'humor'},
			  	{'politicalhumor': 'humor'},

			  	]

sports_subreddits = [
			 
			  	{'nba': 'sports'}, {'sports': 'sports'},
			  	{'nfl': 'sports'}, {'MMA': 'sports'},

			  	]

celebrities_subreddits = [
			 
			  	{'JoeRogan': 'celebrities'}, {'EmmaWatson': 'celebrities'},
			  	{'keanubeingawesome': 'celebrities'}, {'elonmusk': 'celebrities'},

			  	]
discussion_subreddits = [

				{'changemyview': 'discussion'}, {'relationship_advice': 'discussion'},
				{'advice': 'discussion'}, {'amitheasshole': 'discusison'},

				]


subreddits = political_subreddits + academic_subreddits + news_subreddits + gaming_subreddits + geography_subreddits + educational_subreddits +\
ask_subreddits + humor_subreddits + sports_subreddits + celebrities_subreddits + discussion_subreddits

def check_dict():
	print(all([isinstance(i, dict) for i in subreddits]))

#check_dict()