# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 12:24:08 2025

@author: Matth
"""

import os
import tweepy
import re 
import json

# Set up Twitter API (replace with your credentials)
"""
api_key = os.getenv("TwitterAPIKey")
access_token = "YOUR_ACCESS_TOKEN"
access_secret = "YOUR_ACCESS_SECRET"y")
api_secret = os.getenv"TwitterAPIKeySecret"
"""

bearer_token = os.getenv('TwitterBearer')
client = tweepy.Client(bearer_token=bearer_token)


#Get username 
username = "JohnBummit"
#Get tweet ID from tweet url. last digits after \
tweet_id = '1902928424538091671'
#Get User ID
user = client.get_user(username=username, user_fields=["id"])



def extract_user_ids(tweet_id):
    #Retrieve users that replied to tweet
    query = f"conversation_id:{tweet_id}"    

    #Exctract user names replied to a tweet
    replies = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["author_id"])
  

    if replies.data:
        user_ids = [tweet.author_id for tweet in replies.data]
    else:
        print(f"No replies to tweet {tweet_id}")
    
    return user_ids

user_ids = extract_user_ids(tweet_id)
for user_id in user_ids:
    user2 = extract_user_ids(user_id, user_fields=["username"])
 

# Get tweets for a user
def get_tweets(username, count=1):
    tweets = api.user_timeline(screen_name=username, count=count, tweet_mode="extended")
    return [tweet.full_text for tweet in tweets]


# Save JSON to a file
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)  # indent=4 makes it human-readable

print("JSON file created successfully!")
