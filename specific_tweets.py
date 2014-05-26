import json
import os
import sys
import urllib2
import time

'''Assuming this will be our file with the OAuth credentials'''

from twitter.api import Twitter, TwitterError
from twitter.oauth import OAuth, write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

bot_account = ""
CONSUMER_KEY=''
CONSUMER_SECRET=''
OAUTH_TOKEN=''
OAUTH_TOKEN_SECRET=''
twitter = Twitter( auth=OAuth(
                               OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET),
                               secure=True,
                               api_version='1',
                               domain='api.twitter.com')
t2 = twitter


def dayOne():
    t2.statuses.update(status = '@HippieHealthNut Ive been a hippie for over 70 years!')
    t2.statuses.update(status = '@SexyDan23 My son loves your club!')
    t2.statuses.update(status = '@vintagebluechi I love your music :)')
    
def dayThree():
    t2.statuses.update(status = 'My cat scratched me when I moved her off of my keyboard! She doesnt understand that I need to Tweet!!!')
    time.sleep(100)
    t2.statuses.update(status = '@careycorp What is your all time favorite book. I am getting bored and need a new book to read!')
    time.sleep(92)
    t2.statuses.update(status = 'Have you heard of Simon Cat? I saw it on YouTube. Exactly like my cats. I hate them sometimes! http://bit.ly/LaaG8u')
    time.sleep(311)
    t2.statuses.update(status = '@LyssaCurran I cant stop eating apple pie! Help!')
    time.sleep(88)
    t2.statuses.update(status = 'If my cats puke one more time... I am gonna stop feeding them! Just kidding!')
    time.sleep(150)
    t2.statuses.update(status = '@ajpape What is the job market like in Boulder? My grandson might move there')
    time.sleep(132)
    t2.statuses.udpate(status = 'Want to see something funny? Put a jingly collar on a 2 year old cat for the first time.')
    time.sleep(132)
    t2.statuses.update(status = '@KelseyJSutton Love your background. I wish I could figure out how to do that!')
    time.sleep(83)
    t2.statuses.update(status = 'What should I do when my cat chases her sparkle hairball and makes her own fun???')
    time.sleep(54)
    t2.statuses.update(status = '@Scanachi What is your all time favorite movie? Just curious!')
    time.sleep(200)
    t2.statuses.update(status = 'Cats are Goofy Leopards! retweet or mention if you agree... :)')
    time.sleep(67)
    t2.statuses.update(status = '@JeffGodsey What is your favorite movie? Simply curious!')
    
def dayFour():
    t2.statuses.update(status = 'Silly cat - she just started whining and rolling around for no reason. Forgot what movie what I wanted to tweet about!')
    time.sleep(300)
    t2.statuses.update(status = '@baldwinsaint How is the NY weather now? I always wanted to see NY but never got a chance. :(')
    time.sleep(43)
    t2.statuses.update(status = 'Damn you cats! They broke my antique cat statue. I am gonna make a statue out of them!')
    time.sleep(79)
    t2.statuses.update(status = '@leilahlowe Go Yankees! :) Arent they great?')
    time.sleep(402)
    t2.statuses.update(status = 'Bathtub is filled with water and ready for my cats to take a bath with me. ;)')
    time.sleep(325)
    t2.statuses.update(status = '@VanitySized I loved drinking when I was young! Have great stories...')
    
def dayFive():
    t2.statuses.update(status = 'My cats are really dirty. Time to start the washing machine. HAHAHA...')
    time.sleep(69)
    t2.statuses.update(status = '@harper22s I like Jack White. he is very talented. Have you heard his new song?')
    time.sleep(246)
    t2.statuses.update(status = 'Can not believe my cat just chewed the mouse cord. Thank you Dan for bringing your Granny a new mouse.')
    time.sleep(195)
    t2.statuses.update(status = '@ReedEC Where can I find the game 100 floors? Is this a good game for a 12 year old grandson? ')
    time.sleep(221)
    t2.statuses.update(status = 'Finished my cereal box and now my cats have a new toy to play. I am the best Granny ever!')
    time.sleep(99)
    t2.statuses.update(status = '@Purd9685 Can I find your book in Bookstore? I am not good with tech to buy online books. :(')
    
def daySix():
    t2.statuses.update(status = 'I like Nancy to wear makeup. She will be the prettiest cat on the planet.')
    time.sleep(300)
    t2.statuses.update(status = '@SaraTopsyDavis Your profile picture is from a movie... Which one? Cant remember, but I really liked it!')
    time.sleep(92)
    t2.statuses.update(status = 'How can I make my cat de-meowed? i need to have a good night sleep...')
    time.sleep(621)
    t2.statuses.update(status = '@4_eyed_girl your vintage and retro garments are fabulous! Do you sell them in a store?')
    time.sleep(441)
    t2.statuses.update(status = 'I want to have laser cats. They seem to be more useful!')
    time.sleep(427)
    t2.statuses.update(status = '@nealschmitt What is this instagram that shows on your tweets? Is that a camera?')
    
def daySeven():
    t2.statuses.update(status = '@dj_applepeel you have beautiful pictures! Are they from Chicago? Ive never visited Chicago! :(')
    time.sleep(551)
    t2.statuses.update(status = '@allenbusby Do you have any funny jokes? Havent heard one in long time...')
    time.sleep(32)
    t2.statuses.update(status = '@GinaAtch I have two sons and I love movies. Any new movies that you recommend to an old lady to watch?')



if __name__ == "__main__":
    
    if time.strftime('%x') == '05/22/12':
        dayOne()
 
    if time.strftime('%x') == '05/24/12':
        dayTwo()
        
    if time.strftime('%x') == '05/26/12':
        dayThree()

    if time.strftime('%x') == '05/27/12':
        dayFour()
        
    if time.strftime('%x') == '05/28/12':
        dayFive()
        
    if time.strftime('%x') == '05/29/12':
        daySix()
        
