#!/usr/bin/python

import random

class FollowObject:
    
    # This is the constructor
    def __init__(self, t2, ids):
        # Member properties
        self.t2 = t2                                # Twitter Object
        self.ids = ids                              # list of ids of twitter users to follow
        self.result = {}                            # Result
        self.target_user_id = 0
        
    # Member functions  
    def follow(self):       
        try:
            for user_id in self.ids:
                self.result[user_id] = self.t2.friendships.create(user_id=user_id, follow=True)
        except Exception as error:
            print error
            self.result = None
            
        
    def getRandomUserFollowStatus(self, random_ids):
        self.target_user_id = random_ids[random.randrange(0, len(self.ids))]
        user_follow_result = self.result[self.target_user_id]
        if 'status' in user_follow_result:
            text = user_follow_result['status']['text']
        else:
            text = user_follow_result['description']
        print text
        return text
    
    