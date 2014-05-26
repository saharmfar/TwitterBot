#!/usr/bin/python

import json
import urllib2
import argparse
import string
import pickle
import random
import time
import human_responses_map
from setup_twitter import *
from RottenTomatoesHelper import RottenTomatoesHelper
from GoogleHelper import GoogleHelper


if __name__ == '__main__':
	#Set up arg parser
	parser = argparse.ArgumentParser( description = 'Argument parser' )
	parser.add_argument( '-m', action="store_true" )
	parser.add_argument( '-a', action="store_true" )
	#parser.add_argument( '-m', '--morning' )
	#parser.add_argument( '-a', '--afternoon' )
	#parser.add_argument( '-e', '--evening' )
	command_args = parser.parse_args()
	
	#Set up twitter info for authentication
	consumer_key = ''
	consumer_secret = ''
	oauth_token = ''
	oauth_token_secret = ''
	
	loop_count = 0
	while ( loop_count < 2 ):
		#Generate random sleep value to keep posts from occurring at same minute each time
		sleep_time = int( 600 * random.random() )
		time.sleep( sleep_time )
	
		#Morning content
		if ( command_args.m == True ):
			#Generate random tweet message
			cointoss = random.randint(0,1)
			if ( cointoss == 0 ):
				random_tweet = human_responses_map.getRandomTweet()
			else:
				random_tweet = human_responses_map.getRandomTweet2()
			#Post random tweet message
			try:
				t2 = Twitter(auth=OAuth(oauth_token, oauth_token_secret, consumer_key, consumer_secret),secure=True,api_version='1',domain='api.twitter.com')
				status_update = t2.statuses.update(status=random_tweet)
			except:
				print 'Problem tweeting random status update'
			
			
		#Afternoon and evening human status update content
		if ( command_args.a == True ):
			cointoss = random.randint(0,2)
			if ( cointoss == 0 ):
				#News tweet
				prefix = human_responses_map.getRandomNewsPrefix()
			
				try:
					gh = GoogleHelper()
					attempt = gh.google_movie_news_search( prefix )
					if ( attempt == 'success' ):
						print 'Google news search and content tweet successful'
					else:
						print 'Google news search and content tweet not successful'
				except:
					print 'Problem searching Google news and tweeting article'
			else:
				#Tomatoes tweet
				prefix = human_responses_map.getRandomTomatoPrefix()
			
				try:
					rth = RottenTomatoesHelper()
					attempt = rth.rotten_tomatoes_movie_search( prefix )
					if ( attempt == 'success' ):
						print 'Rotten Tomatoes search and content tweet successful'
					else:
						print 'Rotten Tomatoes search and content tweet not successful'
				except:
					print 'Problem searching Rotten Tomatoes and tweeting article'
		loop_count += 1