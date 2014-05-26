#!/usr/bin/python

import random


generic_yes = ["Yes", "Uh huh", "sure", "Absolutely!" , "Yes, dear", "Yes, :)"]
generic_no = ["No", "No, darling", "No, sorry", "No, :(", "No way!"]

'''Loop through these once to avoid duplicates...Add more if necessary'''

random_tweet = ["Today is beautiful", "Another wonderful day",  "Grandma is ready to take on the day", "Where did I leave my favorite purse?", "Why do young people have to drive so fast?" "Everyone, appreciate your grandparents.", "So many movies, so little time", "A little rain makes the flowers grow", "Following comedians on Twitter is great. Gives me laughs all day long.", "Who's better? Blockbuster or Netflix?", "When I was a girl we had the Little Rascals, not Harry Potter or Twilight. Vampires and wizards, gosh!", "Old age is like a plane flying through a storm. Once you're aboard, there's nothing you can do. o Golda Meir", "My grandson told me a joke- When Winnie the Pooh's tiger friend is too crazy, Pooh says Tigger, please!", "Anyone know what pulltab cans are?", "The definition of old age is doing the same thing four or five times and... Where was I going with this?", "Who wins in a duel between the dos equis man and Chuck Norris?", "Maybe I'll try the facebook too", "A study found that Congress speaks at a 10th-grade level", "Remembering today I am a spiritual being having a human experience. And so is everyone else!", "Why do people need to yell?!", "My cat doesn't let me type! Get off!!!"]


random_tweet2 = ["Sometimes I wish I could move to the country", "Watching my favorite movie :)", "Fresh baked applie pie warms my spirit", "I love movies!!", "Retirement sure is relaxing!", "I wonder what's new at the video store?", "Taking the senior bus to the cinema!", "My cat loves to eat!", "I think I'm getting this Twitter thing figured out", "Safeway has a Redbox, but I'm nervous about using my credit card", "Teenage: have time and energy but no money. Working age: have money and energy but no time. Old age: have time and money but no energy!", "If you can dream it, you can do it. Walt Disney", "You cannot stay in your corner of the Forest waiting for others to come to you. You have to go to them sometimes. -Winnie The Pooh", "If a young man honours an older person on account of age, God appoints someone to show reverence to him in his old age", "I click with old people more than I do with people my own age", "I can't believe its 20 years since Johnny Carson's last show", "As a spiritual being, I know that I am here for a spiritual reason. My purpose has to do with my interior life", "My husbands funny. I told him our grandkids were spoiled, he said all kids smell that way"] 


'''Tweets to encourage responses (loop through these'''

incite_response = ["Anyone want to guess my favorite movie?", "Who here has called their grandma today?", "I'm doing my favorite activity...anyone want to guess?", "Hello Twitter! How is everyone today?", "Anyone watch their favorite movie today?"]

'''Message prefixes for news'''
news_prefix = ["Saw this in the news- ", "Getting my entertainment update: ", "Keeping up with the stars! ", "Checking Google, interesting item ", "Neat! ", "Where's the like button for this? ", "Getting my entertainment updates: ", "Looking at movie news, "]

'''Message prefixes for Rotten Tomatoes'''
tom_prefix = ["Did rottentomatoes get this one right? ", "Thinking about seeing this one- ", "Good movie! ", "Great movie! ", "wondering if this will be worth a matinee? ", "think I'm gonna use the senior pass for this one- ", "What art!! ", "Could this be a new classic? ", "Think I'll watch this one again: ", "They just don't make movies like Casablanca anymore... ", "Looking for a good supporting cast and flawless lead acting: "]

'''We would concat the movie name string to any of these sentences'''

movie_talk_part1 = ["Hello, I can tell you saw ", "I noticed you saw the movie ", "I was wondering if you could tell me about ", "Hi, could you give me a recommendation on "]

'''We then concat any of these strings at the end'''

movie_talk_part2 =  [", would it be appropriate for my 13 year old grandson?", ", would my granddaughter enjoy it?", ", is it a good family film?", ", what did you think of it?"]

RTprompts = ["Did rottentomatoes get this one right? ", "This is one of my favorites: ", "Everyone should watch this movie! ", "Retweet if you enjoy this movie! ", "Check this out..."]  

prompts = ["oh my, this is interesting: ", "this is perfect for you, dear :) ", "i found this and thought you'd like it: ", "Hope you like this. Cause I sure did! "]
    
cant_wait = ["i can't wait! ", "can't wait! ", "so excited! ", "this is going to be great!", "looking forward"]

def getRandomNewsPrefix():
		return news_prefix[random.randrange(0, len(news_prefix))]
		
def getRandomTomatoPrefix():
		return tom_prefix[random.randrange(0, len(tom_prefix))]
		
def getRandomGenericYes():
        return generic_yes[random.randrange(0, len(generic_yes))]
    
def getRandomGenericNo():
        return generic_no[random.randrange(0, len(generic_no))]
    
def getRandomTweet():
        return random_tweet[random.randrange(0, len(random_tweet))]

def getRandomTweet2():
        return random_tweet2[random.randrange(0, len(random_tweet2))]
    
def getRandomInciteResponse():
        return incite_response[random.randrange(0, len(incite_response))]
    
def getRandomMovieTalkPart1():
        return movie_talk_part1[random.randrange(0, len(movie_talk_part1))]

def getRandomMovieTalkPart2():
        return movie_talk_part2[random.randrange(0, len(movie_talk_part2))]
    
def getRandomPrompt():
        return prompts[random.randrange(0, len(prompts))]
    
def getRandomCantWait():
        return cant_wait[random.randrange(0, len(cant_wait))]