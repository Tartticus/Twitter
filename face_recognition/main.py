import requests
import os
import tweepy


from PIL import Image
import numpy as np
from io import BytesIO


apikey = os.getenv("TwitterAPIKey")
bearer_token = os.getenv("bearer")


client = tweepy.Client(bearer_token=bearer_token)


query = "word"

# Search tweets and expand user info
response = client.search_recent_tweets(
    query=query,
    max_results=50,
    expansions="author_id",
    user_fields=["id","profile_image_url", "username", "name"]
)

# Get user info from includes
users = {u["id"]: u for u in response.includes["users"]}


def faceplus_analysis(image_url):
    #import api keys
    faceplus_api = os.getenv("faceplusplus_api_key")
    faceplus_secret = os.getenv("faceplusplus_secret")
    
    response = requests.post(
    "https://api-us.faceplusplus.com/facepp/v3/detect",
    data={
        "api_key": faceplus_api,
        "api_secret": faceplus_secret,
        "image_url": image_url,
        "return_attributes": "ethnicity"
    }
)

    print(response.json())


tweets = [] 
profile_pics = []


for tweet in response.data:
    user = users[tweet.author_id]
    print(f"@{user.username} ({user.name})")
    print(f" Profile pic: {user.profile_image_url}")
    print(f"📝 Tweet: {tweet.text}")
    print("-" * 60)

    
    tweets.append({tweet.text:user.profile_image_url})
    faceplus_analysis('https://pbs.twimg.com/profile_images/1932503549813899264/ljC65i_P_400x400.jpg')
    
