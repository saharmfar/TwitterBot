#!usr/bin/python
# May 20, 2012

from twitter.api import Twitter, TwitterError
from twitter.oauth import OAuth, write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

import time
import sys
import json, os, argparse
from pprint import pprint
import random
import plistlib
from plistlib import writePlist
from plistlib import readPlist

import pickle

from SearchObject import SearchObject
from YahooRSSFeed import YahooRSSFeed
from BitlyHelper import BitlyHelper
from FollowObject import FollowObject
from SearchOptimizer import SearchOptimizer

import human_responses_map

CONSUMER_KEY=''
CONSUMER_SECRET=''
OAUTH_TOKEN=''
OAUTH_SECRET=''
    
program_description = "This is our bot!"
parser = argparse.ArgumentParser(description=program_description)
parser.add_argument('-c', '--config_file')
parser.add_argument('-o', '--oauthfile')
args = parser.parse_args()

home_dir = os.environ.get('HOME', '') + os.sep
our_bot_tweet_path = "our_bot.py tweet path: "

def runMain(config_file="our_bot_config.plist", oauthfile=".twitter_oauth"):
    try:
        # Handle config_file
        config_file_path = config_file     
        if os.path.exists(config_file_path):        
            #config = pickle.load(open(config_file_path))
            config = readPlist(config_file_path)
            lastid = config['last_twitter_search_id']
        else:
            config = {} 
            lastid = 0
        
        t1 = getTwitter(1, False, oauth_file=oauthfile)
        t2 = getTwitter(2, False, oauth_file=oauthfile)
          
            
        # THIS SECTION WE NEED TO MODIFY FOR OUR BOT
        print "time before sleep: ", time.localtime()
        tweet_path = random.randrange(0, 40)     
        sleep_time = int( 1200 * random.random() )
        print "time to sleep: ", sleep_time
        time.sleep( sleep_time )        
        print "time after sleep: ", time.localtime()
        
        bitlyHelper = BitlyHelper()
        yahoo_rss = YahooRSSFeed()
        search_obj = SearchObject(t1, getRandomMovieTitleAsList())
        
        # Follow 2 target users
        random_ids = getRandomTargetIds(2)
        follow_obj = FollowObject(t2, random_ids)
        follow_obj.follow()
        
        if tweet_path >= 0 and tweet_path <= 5:
            print our_bot_tweet_path + str(tweet_path)
            copyRandomUserTweetBasedOnMovie(t1, t2)                
        elif tweet_path == 6:
            print our_bot_tweet_path + str(tweet_path)
            doTweet(t2, (human_responses_map.getRandomCantWait() + yahoo_rss.getRandomMovieOpens()))
        elif tweet_path == 7:
            print our_bot_tweet_path + str(tweet_path)
            doTweet(t2, yahoo_rss.getRandomMovieSummary())
        elif tweet_path >= 8 and tweet_path <= 12:
            print our_bot_tweet_path + str(tweet_path)
            doTweet(t2, yahoo_rss.getRandomNewsLink())                
        
        if follow_obj.result != None:
            if tweet_path == 13:
                print our_bot_tweet_path + str(tweet_path)
                search_text = follow_obj.getRandomUserFollowStatus(random_ids)
                suggested_link = yahoo_rss.doYahooSearchReturnLink(search_text.split())
                short_link = bitlyHelper.getShortenedLink(suggested_link)
                screen_name = getScreenNameFromUserId(t2, follow_obj.target_user_id)
                doAtTweetWithLink(t2, screen_name, short_link)
        
        if tweet_path == 14:
            print our_bot_tweet_path + str(tweet_path)
            search_opt = SearchOptimizer()
            random_id = getRandomTargetId()
            screen_name = getScreenNameFromUserId(t2, random_id)        
            user_statuses_text = getUserStatusesText(t2, random_id, 200)                
            search_words = search_opt.getRandomOptimalSearchWords(user_statuses_text)
            suggested_link = yahoo_rss.doYahooSearchReturnLink(search_words.split())
            short_link = bitlyHelper.getShortenedLink(suggested_link)
            doAtTweetWithLink(t2, screen_name, short_link)
            
        elif tweet_path >= 15 and tweet_path <= 18:
            print our_bot_tweet_path + str(tweet_path)
            random_id = getRandomTargetId()
            screen_name = getScreenNameFromUserId(t2, random_id)
            doAtTweet(t2, screen_name, human_responses_map.getRandomMovieTalkPart1() + getRandomMovieTitle() + human_responses_map.getRandomMovieTalkPart2())
        
        elif tweet_path >= 19 and tweet_path <= 38:
            print our_bot_tweet_path + str(tweet_path)
            retweetFromTimeline(t2)
            
        print "finishing our_bot.py script: ", time.localtime()
        
        # END OF SECTION TO MODIFY        
        
        # rewrite config_file
        if search_obj.since_id > 0:
            config['last_twitter_search_id'] = search_obj.since_id        
            writePlist(config, config_file_path)
        
    except TwitterError as error:
        "There was a TwitterError"
        print error    
    except IOError as error:
        "There was an IOError"
        print error
    except Exception as error:
        "There was an error"
        print error
        
def retweetFromTimeline(t2):
    result = t2.statuses.home_timeline(count=200, exclude_replies=True)
    tweet_id = result[random.randrange(0, len(result))]['id_str']
    rt_result = t2.statuses.retweet(id=tweet_id)
    
def copyRandomUserTweetBasedOnMovie(t1, t2):
    search_obj = SearchObject(t1, getRandomMovieTitleAsList())
    search_obj.runSearch()
    doTweet(t2, search_obj.getRandomTweetText())
        
def getMoviesList():
    # pickle was not working for me
    with open( 'newmovies.txt', 'r' ) as f:
        lines = f.readlines()
    movies = []
    for line in range(1, len(lines), 2):
        line = lines[line]
        movies.append(line[line.find("'") + 1:line.rfind("'") - 2])
    return movies

def getRandomMovieTitle():
    movies = getMoviesList()
    return movies[random.randrange(0, len(movies))]

def getRandomMovieTitleAsList():
    movies = getMoviesList()
    randmovie = movies[random.randrange(0, len(movies))]
    return [randmovie]
    

def getUserStatusesText(t2, user_id, count):
    user_statuses = t2.statuses.user_timeline(user_id=user_id, count=count)
    users_tweets = ""
    for status in user_statuses:
        users_tweets += status['text'] + ' '
    return users_tweets

def getScreenNameFromUserId(t2, user_id):
    result = t2.users.show(user_id=user_id)
    return result['screen_name']

def doTweet(t2, text):
    if len(text) > 130:
        t2.statuses.update(status=text[:130] + '...')
    else:
        t2.statuses.update(status=text)
    
def doAtTweet(t2, username, text):
    if len(text) > 120:
        t2.statuses.update(status="@%s %s" % (username, text[:120] + '...'))
    else:
        t2.statuses.update(status="@%s %s" % (username, text))

def doAtTweetWithLink(t2, username, link):
    prompt = human_responses_map.getRandomPrompt()
    t2.statuses.update(status="@%s %s %s" % (username, prompt, link.replace('\\', '')))
    
def getRandomTargetId():
    randomIds = getRandomTargetIds(1)
    return randomIds[0]
    
def getRandomTargetIds(qty):
    with open('target_user_ids.json') as f:
        user_ids = json.loads(f.read())
    random_ids = []
    i = 0
    while i < qty:
        random_ids.append(user_ids[random.randrange(0, 500)])
        i += 1
    return list(set(random_ids))
    
def doRetweets(t2, tweets, username):
    for tweet in tweets:
        text = tweet['text']
        tweeter = tweet['from_user']
        if isRTR(text, username):
            newTweet = getRetweetText(username, text, tweeter)
            t2.statuses.update(status=newTweet)                

def getRetweetText(username, text, tweeter):
    newTweet = "RT @%s %s" % (tweeter, text[len(username) + 6:]) 
    return newTweet
    
def isRTR(text, username):
    return (text[len(username) + 2:len(username) + 6] == 'RTR ')

def getTwitter(oneOrTwo, useOauthFile, oauth_file='.twitter_oauth'):
    oauth_filename = home_dir + oauth_file
    try:
        oauth_token, oauth_token_secret = read_token_file( oauth_filename )
    except IOError:
        print 'OAuth file {} not found'.format( oauth_filename )
        response = raw_input( 'Do you want to initiate a new oauth dance (y or n)? ' )
        if not ( len( response ) > 0 and response[0].upper() == 'Y' ):
            oauth_token = oauth_token_secret = ''
        else:  
            oauth_token, oauth_token_secret = oauth_dance('Clever App Name', CONSUMER_KEY, CONSUMER_SECRET, token_filename=oauth_filename)
    
    try:
        if oneOrTwo == 1:
            return Twitter(domain='search.twitter.com')
        elif oneOrTwo == 2:
            if useOauthFile:
                return Twitter(
                         auth=OAuth(
                                    oauth_token, oauth_token_secret, CONSUMER_KEY, CONSUMER_SECRET),
                         secure=True,
                         api_version='1',
                         domain='api.twitter.com')
            else:
                return Twitter(
                         auth=OAuth(
                                    OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET),
                         secure=True,
                         api_version='1',
                         domain='api.twitter.com')
        else:         	
            return False

    except TwitterError as error:
        "There was a TwitterError"		
        print error    
        return False
    except IOError as error:
        "There was an IOError"
        print error
        return False
    except Exception as error:
        "There was an error"
        print error
        return False
        

if __name__ == '__main__':
    config_file = "our_bot_config.plist"
    oauthfile = ".twitter_oauth"
    
    if vars(args):
        args = vars(args)
        if args['config_file']:
            config_file = args['config_file']
        if args['oauthfile']:
            oauthfile = args['oauthfile']
            
    runMain(config_file=config_file, oauthfile=oauthfile)
    
    