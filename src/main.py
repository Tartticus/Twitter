# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 12:24:08 2025

@author: Matth
"""

import os
import tweepy
import re 
import json
import requests
from nltk import string, stopwords, PorterStemmer
# Set up Twitter API (replace with your credentials)
"""
api_key = os.getenv("TwitterAPIKey")
access_token = "YOUR_ACCESS_TOKEN"
access_secret = "YOUR_ACCESS_SECRET"y")
api_secret = os.getenv"TwitterAPIKeySecret"
"""





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


    
 

def get_username(USER_ID, Bearer_Token):
    # Twitter API endpoint to get user info by ID
    url = f"https://api.twitter.com/2/users/{USER_ID}"
    
    # Set up authorization headers
    headers = {"Authorization": f"Bearer {Bearer_Token}"}
    
    # Make the request
    response = requests.get(url, headers=headers)
    
    # Parse response
    if response.status_code == 200:
        user_data = response.json()
        username = user_data["data"]["username"]
        print(f"Username: {username}")
    else:
        print(f"Error: {response.status_code}, {response.json()}")


def preprocess_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    
    tokens = text.split()

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]

    # Join tokens back into a single string
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

# Get tweets for a user
def get_tweets(username, count=1):
    
    #query to retrieve
    query = f"from:{username}"  
    tweet  = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["author_id"])
    tweet = preprocess_text(tweet)
    data.append([username,tweet])
    return data

      

data = []


# Save JSON to a file
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)  # indent=4 makes it human-readable

print("JSON file created successfully!")


bearer_token = os.getenv('TwitterBearer')
client = tweepy.Client(bearer_token=bearer_token)


#Get username 
username = "JohnBummit"
#Get tweet ID from tweet url. last digits after \
tweet_id = '1902928424538091671'

def main():
    users = []
    user_ids =extract_user_ids(tweet_id)
    #Get User ID
    for user in user_ids:
        user = client.get_user(username=username, user_fields=["id"])
        users.append(users)
    for user in users:
        get_username(user, bearer_token)
        get_tweets(user, 1)
        
