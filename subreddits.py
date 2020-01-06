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
			  	{'pathofexile': 'gaming'}, {'cyberpunkgame': 'gaming'},
			  	{'DnD': 'gaming'},

			  	]

internet_and_apps_subreddits = [

				{'InternetIsBeautiful': 'internet and apps'}, {'facepalm': 'internet and apps'},
				{'4chan': 'internet and apps'}, {'robinhood': 'internet and apps'},
				{'greentext': 'internet and apps'}, {'oldpeoplefacebook': 'internet and apps'},
				{'blackpeopletwitter': 'internet and apps'}, {'WhitePeopleTwitter': 'internet and apps'},
				{'tumblrinaction': 'internet and apps'},
				
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
				{'advice': 'discussion'}, {'amitheasshole': 'discussion'},

				]

entertainment_subreddits = [
				
				{'entertainment': 'entertainment'}, {'fantheories': 'entertainment'},
				{'Disney': 'entertainment'}, {'anime': 'entertainment'}, 
				{'manga': 'entertainment'}, {'Books': 'entertainment'}, 
				{'freefolk': 'entertainment'}, {'lotr': 'entertainment'},

				]

lifestyle_subreddits = [

					{'LifeProTips': 'lifestyle'}, {'lifehacks': 'lifestyle'},
					{'geek': 'lifestyle'},

					]

community_subreddits = [

					{'teenagers': 'communities'}, {'introvert': 'communities'},
					{'teachers': 'communities'}, {'lgbt': 'communities'},
					{'gaybros': 'communities'}, {'actuallesbians': 'communities'}

					]

religion_subreddits = [

					{'Psychonaut': 'religion and beliefs'}, {'Buddhism': 'religion and beliefs'},
					{'Stoicism': 'religion and beliefs'}, {'atheism': 'religion and beliefs'},
					{'Christianity': 'religion and beliefs'}, {'philosophy': 'religion and beliefs'},

					]


subreddits = political_subreddits + academic_subreddits + news_subreddits + gaming_subreddits + geography_subreddits + educational_subreddits +\
ask_subreddits + humor_subreddits + sports_subreddits + celebrities_subreddits + discussion_subreddits + religion_subreddits + community_subreddits+\
lifestyle_subreddits + entertainment_subreddits + internet_and_apps_subreddits 

def check_dict():
	print(all([isinstance(i, dict) for i in subreddits]))
	print(len([i for i in subreddits]))

#check_dict()