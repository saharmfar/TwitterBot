import json
import urllib2
import string
import pickle
import random

def findMovieInTweet(theTweet):
    
    theTweet = theTweet + '\n'
    
    theTweet = theTweet.replace('!', '')
    theTweet = theTweet.replace('.', '')
    theTweet = theTweet.replace('#', '')
    theTweet = theTweet.replace('?', '')
    theTweet = theTweet.replace('"', '')
    
    movieList = open ('newMovies.txt', 'r')
    
    tweetUpper = theTweet.upper()
    
    for eachLine in movieList:
                
        eachLineUpper = eachLine.upper()
        
        tweetIndex = tweetUpper.find(eachLineUpper)
        
        if tweetIndex != -1:
            for i in range (tweetIndex, len(tweetUpper)):
                print tweetUpper[i]        
    
    

    
findMovieInTweet('this is the avengers!\n')