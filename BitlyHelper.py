#!/usr/bin/python

import urllib
import urllib2

class BitlyHelper:
    
    def __init__(self):
        self.bitly_api = "http://api.bitly.com"
        self.username = "mikehitchcock45"
        self.api_key = "R_aaf68f9d5dc5d07ad2648fbaaf89b76f"        
        self.shorten = "/v3/shorten?longUrl=%s&login=%s&apiKey=%s" 
        
    def getShortenedLink(self, link):
        url = self.bitly_api + self.shorten % (link, self.username, self.api_key)
        response = urllib2.urlopen(url)
        f = eval(response.read())
        short = f['data']['url']
        return short.replace('\\', '')