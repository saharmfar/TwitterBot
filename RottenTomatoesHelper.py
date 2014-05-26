#!/usr/bin/python

import json
import urllib2
import string
import pickle
import random
from setup_twitter import *

class RottenTomatoesHelper:

	def __init__( self ):
		#Establish variables
		self.rotten_tomatoes_space = '+'
		self.rotten_tomatoes_url_base = ''
		self.rotten_tomatoes_paging = '&page_limit=1&page=1'
		self.consumer_key = ''
		self.consumer_secret = ''
		self.oauth_token = ''
		self.oauth_token_secret = ''	


	def rotten_tomatoes_movie_search( self, msgprefix ):
		try:
			#Set up Twitter API
			t2 = Twitter(auth=OAuth(self.oauth_token, self.oauth_token_secret, self.consumer_key, self.consumer_secret),secure=True,api_version='1',domain='api.twitter.com')
			
			#Open newmovies.txt to load movie title list from pickle
			newmovies = open( 'newmovies.txt', 'r' )
			movies = pickle.load( newmovies )
			newmovies.close()
			
			#Generate random number for random title selection
			randindex = int( len( movies ) * random.random() )
	
			#Get random title
			randomtitle = movies.pop( randindex )
			
			#Chomp endline character
			randomtitle = randomtitle.rstrip( '\n' )
	
			#Convert spaces in title to + for search
			if ( string.find( randomtitle, ' ' ) != -1 ):
				randomtitle = string.replace( randomtitle, ' ', self.rotten_tomatoes_space )
			
			#Perform Rotten Tomatoes search
			tomatoes_url = self.rotten_tomatoes_url_base + randomtitle + self.rotten_tomatoes_paging
			tomatoes_request = urllib2.urlopen( tomatoes_url )
			tomatoes_response = tomatoes_request.read()
			movie = json.loads( tomatoes_response )
			movietitle = movie['movies'][0]['title']
			movieurl = movie['movies'][0]['links']['alternate']
			
			#Post result to Twitter status update
			status_update = t2.statuses.update(status=msgprefix + movietitle + ' ' + movieurl)
			
			#Deserialize movies list back to file
			newmovies = open( 'newmovies.txt', 'w' )
			pickle.dump( movies, newmovies )
			newmovies.close()
			
			#Write used title to oldmovies text file to track
			oldmovies = open( 'oldmovies.txt', 'a' )
			oldmovies.write( randomtitle + '\n' )
			oldmovies.close()
			
			#Return response indicating success
			return 'success'
		except:
			#Error encountered, return response indicating error
			return 'error'
