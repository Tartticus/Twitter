import requests
import os
import tweepy
import numpy as np
from grok_response import twitter_ai_response
from datetime import datetime
import duckdb

def create_client():
    apikey = os.getenv("TwitterAPIKey")
    apisecret = os.getenv("TwitterAPIKeysecret")
    bearer_token = os.getenv("bearer")
    access_token = os.getenv("TwitterAccessToken")
    access_secret = os.getenv("TwitterAccessSecret")
    
    client = tweepy.Client(bearer_token=bearer_token,
                           consumer_key=apikey,
                           consumer_secret=apisecret,
                           access_token=access_token,
                           access_token_secret=access_secret)
    return client


def twitter_get_responded_tweets(results=10):
    twitter_id = '1576918997781446656'
    #search tweets I was @tted in
    query = "@JohnBummit"
    
    # Search tweets and expand user info
    response = client.search_recent_tweets(
        query=query,
        max_results=results,
        expansions=["author_id"],
        user_fields=["id","profile_image_url", "username", "name"]
    )
    
    tweet_replies = []
    for tweet in response.data:
        tweet_text = tweet.text
        tweet_id = tweet.id
        
        #check reply search, if its been replied to, then go next
        if search_for_reply(tweet.id,tweet.text):
            continue
        else:
            #append tweets that dont have a reply
            #make sure we dont reply to our own tweet 
            if not tweet.author_id == twitter_id:
                tweet_replies.append({tweet_id:tweet_text})
    return tweet_replies         
        
 
def search_for_reply(tweet_id,tweet):
    #see if I responded
    author_id = '1576918997781446656'
    query = f"conversation_id:{tweet_id} -from:{author_id}"
    
    response = client.search_recent_tweets(
        query=query,
        tweet_fields=["author_id", "in_reply_to_user_id", "conversation_id", "created_at", "text"],
        max_results=50
    )
    
    if response.data:
        return True
    else:
        print("No replies found.")    




def reply_to_tweet(tweet_id_reply,response):
    try:
        response = client.create_tweet(
        text=response,
        in_reply_to_tweet_id=tweet_id_reply
        )
        print("Reply posted\n")
    except Exception as e:
       print(f"Reply failed: {e}")
    
    
def main():
    #connect to db to save tweets
    conn = duckdb.connect('Tweets.duckdb')
    client = create_client()
    global client
    
    tweets = twitter_get_responded_tweets()
    for index, item in enumerate(tweets):
        for key, value in item.items():
            response = twitter_ai_response(value)
            try:
                reply_to_tweet(key,response)
                datetime = datetime.now()
                conn.execute("INSERT INTO Tweet_Replies (datetime, tweet_id,tweet, reply) VALUES (?,?,?,?)",[datetime,key,value,response])
                print("insert_successful")
            except Exception as e:
                print(f'Reply failed: {e}')
    
