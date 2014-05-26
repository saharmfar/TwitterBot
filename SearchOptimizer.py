#!/usr/bin/python

import random
import operator

class SearchOptimizer:
    
    # This is the constructor
    def __init__(self):        
        self.exclude_words = ['to', 'a', 'the', 'my', 'I', '-', 'be', 'new', 'so',
                              'that', 'if', 'need', 'feel', 'want', 'me', 'go', 'out', 
                              'an', 'some', 'has', 'had', 'by', 'all', 'was',
                              'what', 'been', 'used', 'do', 'week', 'haha']
        
    def getRandomOptimalSearchWords(self, text):
        words = text.split()
        for (i, word) in enumerate(words):
            words[i] = word.replace('.', '').replace('!', '').replace(',', '').lower()
        
        words_counter = {}
        for word in words:
            if word in words_counter:
                words_counter[word] += 1
            else:
                words_counter[word] = 1
        
        sorted_words = sorted(words_counter.iteritems(), key=operator.itemgetter(1))
        #print sorted_words
        searchwords = ""
        i = 0
        while i < 6:            
            random_index = random.randrange(int(len(sorted_words) * 0.5), int(len(sorted_words) * 0.9))
            searchword = sorted_words[random_index][0]
            if searchword not in self.exclude_words and len(searchword) > 3:
                searchwords += searchword + " "
                i += 1 
        return searchwords
    
    
                
        
        