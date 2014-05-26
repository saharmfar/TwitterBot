#!usr/bin/python
# execute daily by cron

# Ed Smith
# Mike Hitchcock
# Sahar Massoud Far
# Garet Anderson
# Daniel Nanadjanians
# May 20, 2012

from twitter.api import Twitter, TwitterError
from twitter.oauth import OAuth, write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

import time, sys, urllib2
import json, os
import random # random.randrange(0, 500)
import plistlib
from plistlib import writePlist
from plistlib import readPlist

## bot credentials go here!
bot_account = ""
CONSUMER_KEY=''
CONSUMER_SECRET=''
OAUTH_TOKEN=''
OAUTH_TOKEN_SECRET=''

# args
program_description = "This is our bot's friendly script!"
parser = argparse.ArgumentParser(description=program_description)
parser.add_argument('-t', '--target_user_file')
args = parser.parse_args()

# vars
home_dir = os.environ.get('HOME', '') + os.sep
config_file=".ourbot_target_users"
daily_target_percent = 25 # percent

# funcs
def first_list_minus_second(first_list, second):
    return_this = first_list[:]
    for item in second:
        if item in return_this:
            return_this.remove(item)
    return return_this

def get_followers(screen_name):
    ''' returns list of followers '''
    user_ids = []
    next_cursor_str = '-1'
    while next_cursor_str != '0':
        try:
          s = 'http://api.twitter.com/1/friends/ids.json?screen_name={}&cursor={}'
          f = urllib2.urlopen( s.format( screen_name, next_cursor_str ) )
          new_user_ids_str = f.read()
          new_user_ids_obj = json.loads( new_user_ids_str )
          new_user_ids = new_user_ids_obj['ids']
          user_ids = user_ids + new_user_ids
          next_cursor_str = new_user_ids_obj['next_cursor_str']
        except urllib2.URLError:
          print 'URLError'
          return []
        except ValueError:
          print 'ValueError'
          return []
    return user_ids

def follow(user_id):
    try:
        return twitter.friendships.create(user_id=user_id, follow=True)
    except TwitterError as error:
        "There was a TwitterError when following"
        print error

def unfollow(user_id):
    try:
        return twitter.friendships.destroy(user_id=user_id)
    except TwitterError as error:
        "There was a TwitterError when unfollowing"
        print error

## Get target data from file
try:
    if os.path.exists(config_file):        
        user_data = readPlist(config_file)
    elif os.path.exists(home_dir + config_file):
        user_data = readPlist(home_dir + config_file)
    else:
        print "Could not find target friend list?!?!?!?!"
        print config_file
        ## building our a target list dictionary as shown here...
        user_data = {}
        user_list = json.loads( file( 'target_user_ids.json' ).read() )
        for user in user_list:
            user_data[user] = -1 #represents days since followed
except IOError as error:
        "There was an IOError reading the file"
        print config_file
        print error

## Connect to twitter
try:
    twitter = Twitter( auth=OAuth(
                                OAUTH_TOKEN, OAUTH_TOKEN_SECRET, 
                                CONSUMER_KEY, CONSUMER_SECRET),
                     secure=True,
                     api_version='1',
                     domain='api.twitter.com')
except TwitterError as error:
    "There was a TwitterError when connecting"
    print error
    exit()

bot_followers = get_followers(bot_account)
target_users = first_list_minus_second(user_data.keys(), bot_followers)

followed_today = 0;
already_inspected_users = []
while(followed_today < len(target_users) * daily_target_percent / 100.0 ):
    random_index = random.randrange(0, len(target_users))
    random_user = user_data.keys()[random_index]
    if random_user not in already_inspected_users:
        already_inspected_users.append( random_user )
        # have we already followed this person?
        if (user_data[ random_user ] > 3):
            print "unfollowing:", random_user
            results = unfollow(random_user)
            user_data[ random_user ]= -1
        # change this to elif, to disable refollow harrassment features
        if (user_data[ random_user ] < 0):
            print "following:", random_user
            results = follow(random_user)
            user_data[ random_user ]= 0
        else:
            user_data[ random_user ]= user_data[ random_user ] + 1


#save results
writePlist(config, config_file)

