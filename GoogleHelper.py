#!/usr/bin/python

import json
import urllib2
import string
from setup_twitter import *

class GoogleHelper:

	def __init__( self ):
		#Establish variables
		self.google_space = '%20'
		self.google_url_base = 'https://ajax.googleapis.com/ajax/services/search/news?v=1.0&q='
		self.consumer_key = ''
		self.consumer_secret = ''
		self.oauth_token = ''
		self.oauth_token_secret = ''
	
	def google_movie_news_search( self, msgprefix ):
		try:
			#Set up Twitter API
			t2 = Twitter(auth=OAuth(self.oauth_token, self.oauth_token_secret, self.consumer_key, self.consumer_secret),secure=True,api_version='1',domain='api.twitter.com')
		
			#Perform Google news search for movies news- search term 'movies'
			search_term = 'movies'
			google_url = self.google_url_base + search_term
			gnews_request = urllib2.urlopen( google_url )
			gnews_response = gnews_request.read()
			movienews = json.loads( gnews_response )
			article_title = movienews['responseData']['results'][0]['titleNoFormatting']
			article_url = movienews['responseData']['results'][0]['unescapedUrl']
		
			#Post status update for news article
			status_update = t2.statuses.update(status=msgprefix + article_title + ' ' + article_url)
		
			#Return response indicating success
			return 'success'
		
		except:
			#Return response indicating error
			return 'error'