#!/usr/bin/python

import random

class SearchObject:
    
    # This is the constructor
    def __init__(self, t1, args, since_id=0, include_entities=False):
        # Member properties
        self.t1 = t1                                # Twitter Search Object        
        self.args = args                            # Args in search format - this is a List of Strings
        self.format = self.getFormat()                 # String format for search
        self.since_id = since_id                    # Only return results after since_id
        self.include_entities = include_entities    # include_entities in Search?
        self.result = {}                            # Result
      
    # Member functions  
    def runSearch(self):        
        self.result = self.t1.search(q=self.getSearchQuery(), since_id=self.since_id, include_entities=self.include_entities, lang='en')
        self.setSinceId()
        
    def getSearchQuery(self):
        return self.format % tuple(self.args)
    
    def setSinceId(self):
        self.since_id = self.result['refresh_url']        
        self.since_id = self.since_id[10:self.since_id.find('&')]
        
    def getTweets(self):
        return self.result['results']
    
    def getFormat(self):
        format = ""
        for arg in self.args:
            format += "%s "
        return format
    
    def getRandomTweetText(self):
        tweets = self.getTweets()
        tweet = tweets[random.randrange(0, len(tweets))]['text']
        return tweet.replace('&amp;', '&')
        
        
        