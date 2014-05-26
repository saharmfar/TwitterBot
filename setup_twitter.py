from twitter.api import Twitter, TwitterError
from twitter.oauth import OAuth, write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

import os
import time
import sys

CONSUMER_KEY=''
CONSUMER_SECRET=''

oauth_filename = os.environ.get( 'HOME', '' ) + os.sep + '.twitter_oauth'
try:
  oauth_token, oauth_token_secret = read_token_file( oauth_filename )
except IOError:
  print 'OAuth file {} not found'.format( oauth_filename )
  response = raw_input( 'Do you want to initiate a new oauth dance (y or n)? ' )
  if not ( len( response ) > 0 and response[0].upper() == 'Y' ):
    oauth_token = oauth_token_secret = ''
  else: 
    oauth_token, oauth_token_secret = oauth_dance('Clever App Name', CONSUMER_KEY, CONSUMER_SECRET, token_filename=oauth_filename)

t1 = Twitter(domain='search.twitter.com')
t2 = Twitter(
  auth=OAuth(
     oauth_token, oauth_token_secret, CONSUMER_KEY, CONSUMER_SECRET),
  secure=True,
  api_version='1',
  domain='api.twitter.com')