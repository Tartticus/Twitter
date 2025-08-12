# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 12:31:32 2025

@author: matth
"""

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver
import time
import requests
import re
import os
from selenium.common.exceptions import NoSuchElementException
#import message sending logic
import random
import string
# Niggabot token
token = 'MTI5OTU2NDA5MzQ1OTY2MDkyMQ.GALqAi.L7Glh0DKB8Q_cVrs9nfCl8EFDNO0nynHxi8Pzk'

#make sure to get your cookies
def twitter_login():
    # Open X
    driver.get("https://x.com/")
    # Step 1: Define your cookies from the browser
    cookies = [
        {
            "name": "auth_token",
            "value": "f71e1af86f30900e0656d15fbbfe9ed2e8d41255",
            "domain": ".x.com"
        },
        # Add more cookies if necessary
    ]
    # Step 5: Add your cookies to the session
    for cookie in cookies:
        driver.add_cookie(cookie)

    # Step 6: Refresh the page so that cookies take effect
    driver.refresh()
 
    


def twitter_search(URL):
    #Open Twitter
    # Open Twitter
    driver.get(URL)
    
    # Pause for page to load
    time.sleep(7)
    
    
    # Get the text of the top tweet
    driver.execute_script("window.scrollBy(0, 500);")
    top_tweet2 = driver.find_element(By.XPATH, '//div[@data-testid="tweetText"]//span').text
    top_tweet = driver.find_element(By.XPATH, '(//article[@data-testid="tweet"])[2]//div[@data-testid="tweetText"]').text
    
    
    tweet = top_tweet
    print("tweet",tweet)
    return tweet



def twitter_ai_response(tweet):
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer xai-ocUezT9HktjhMYxMEhypg6H8vBfASkHNFbA0MSWCWQF6CeXimf4910GVbw57dvv0ok0MIWVIx6xCDS9q"
    }
    
    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are a 15 year obese minecraft player"
            },
            {
                "role": "user",
                "content": f"Respond to this like you would respond to a tweet kinda angrily. Tell them they are bald, and spearmint is the best zyn. no hashtags: {tweet}"
            }
        ],
        "best_of": 4,
        "model": "grok-4",
        "stream": False,
        "temperature": 0,
        "top_p": 0.1,
        "temperature": 0
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    Test = response.json()
    
    content = Test['choices'][0]['message']['content']
    
    
    return content

def tweet_reply(response, image_path=None):
    #cloick the tweet
    tweet = driver.find_element(By.XPATH, '(//article[@data-testid="tweet"])[2]//div[@data-testid="tweetText"]')  # Select the second tweet to avoid pinned tweet
    tweet.click()
    
    # Lets goooo
    time.sleep(4)
    
    
    
    reply_box = driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
    
    # Click the reply button first to reveal the image input
    reply_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,  '//div[@data-testid="tweetTextarea_0"]')))
    reply_box.click()
    
    
    
    if image_path and isinstance(image_path, str) and os.path.isfile(image_path):
        # Check if there is an image to upload
        # Locate the hidden file input element for the image upload
        upload_button = driver.find_element(By.XPATH, '//input[@type="file"]')
           
        # Use JavaScript to make the input element visible
        driver.execute_script("arguments[0].style.display = 'block';", upload_button)

           
        # Now, send the file path to the upload element
        upload_button.send_keys(image_path)
        print("Troll image uploaded")
        time.sleep(8)
    
       
        
        
    #function to remove emojis (not supported by selenium)
    def remove_non_bmp_characters(text):
        return re.sub(r'[^\u0000-\uFFFF]', '', text)
    response = remove_non_bmp_characters(response)
    #response gets processed here
    reply_text = response
    
    reply_box.send_keys(reply_text)
   

    reply_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@data-testid='tweetButtonInline']"))
    )
    
    driver.execute_script("arguments[0].click();", reply_button)

    # Optionally, wait a few seconds to observe the result before closing the browser
    WebDriverWait(driver, 5)
   
    
    time.sleep(8)
    return


# a function that nukes dudes you dont like
def internet_terrorist(tweet, image_path=None, repeat_count=1):
    #cloick the tweet
    tweet = driver.find_element(By.XPATH, '(//article[@data-testid="tweet"])[2]//div[@data-testid="tweetText"]')  # Select the second tweet to avoid pinned tweet
    tweet.click()
    
    # Lets goooo
    time.sleep(4)
    
    
    
    for _ in range(repeat_count):
        #generate Ai repsonse
        response = twitter_ai_response(tweet)
        
        #response gets processed here
        reply_box = driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
        
        # Click the reply button first to reveal the image input
        reply_box = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,  '//div[@data-testid="tweetTextarea_0"]')))
        reply_box.click()
        #function to remove emojis (not supported by selenium)
        def remove_non_bmp_characters(text):
            return re.sub(r'[^\u0000-\uFFFF]', '', text)
        response = remove_non_bmp_characters(response)
        
        #Bypass Elon filter
        random_char = random.choice(string.ascii_letters) 
        # Choose a random position in the string
        position = random.randint(0, len(response))
        # Insert the random character at the chosen position
        response = response[:position] + random_char + response[position:]
        
        
        if image_path and isinstance(image_path, str) and os.path.isfile(image_path):
            # Check if there is an image to upload
            # Locate the hidden file input element for the image upload
            upload_button = driver.find_element(By.XPATH, '//input[@type="file"]')
               
            # Use JavaScript to make the input element visible
            driver.execute_script("arguments[0].style.display = 'block';", upload_button)
    
               
            # Now, send the file path to the upload element
            upload_button.send_keys(image_path)
            print("Troll image uploaded")
            time.sleep(3)
        
           
            
        print(f"AI Response: {response}\n")    
        
        reply_text = response
        # Use JavaScript to focus on the reply box
        driver.execute_script("arguments[0].focus();", reply_box)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,  '//div[@data-testid="tweetTextarea_0"]')))
        time.sleep(0.5)
        reply_box.send_keys(reply_text)
       
    
        reply_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@data-testid='tweetButtonInline']"))
        )
        
        driver.execute_script("arguments[0].click();", reply_button)
        
    
        # Optionally, wait a few seconds to observe the result before closing the browser
        time.sleep(1)
        driver.get(driver.current_url)
        time.sleep(3)
       
    return


def troll_nuke(reply,image):    
    count2 = 0
    #logic to troll extra hard if needed and break the loop
    channel_id = '1299633437774315583' 
    if count2 == troll_param:
         
         reply = "This you, nigga?" 
         image = r"trollpics\Troll.jpg"
         replyresponse = reply
         troll_loop = 0
         try:
             tweet_reply(reply,image)
             if image:
                 reply = reply +", With image"
             print(f"Troll post posted: {reply}\n")
             send_message(channel_id,f"Troll posts sent to {username}: {reply}",token)
         except Exception as e:
             print(e)
         #trrolling loop logic to keep it in here if   it was a troll loop
         if troll_loop == troll_param:
             troll_loop = 0
             count2 = 0
             
         troll_loop +=1
         time.sleep(6)
         return
     
# List to store the tweets we have replied to
replied_tweets_dict = {}

chrome_options = Options()

headless =  input("Would you like to start in headless mode?: 1 for yes, 2 for no\n")
if headless == '1':
    chrome_options.add_argument("--headless")  # Enables headless mode
chrome_options.add_argument("--window-size=1920,1080") 
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)


def main(usernames):
    #timing
    start_time = time.time()
    #Channel_ID for discord
    channel_id = '1299633437774315583' 
    
    
    #Initialize choice to skip first tweet, use if restarting fast
    
    options = ["1","2"]
    choice = input("Would you like to skip the first tweet?: 1 for yes, 2 for no\n")
    troll_param = input("How Many times would you like to spam per user?\n")
    troll_param = int(troll_param)
      
    count = 0 #count to keep track
    
    # Login to twitter (put cookies here)
    twitter_login()
    # Keep running this to check for new tweets and replyGGGGGG
    while True:
        for username in usernames:
            print(f"Terrorizing {username}\n")
            URL = f"https://x.com/{username}"
            
            tweet = twitter_search(URL)
            
            try:
                #nuking funciton
                internet_terrorist(tweet,None, troll_param)
            except Exception as e:
                print(e)
                continue
        #counter to keep track
        count += 1
        
       
        end_time = time.time()
        elapsed_time = round((end_time - start_time),2)
        print(f"{count} iterations so far\n Total time elasped: {elapsed_time} seconds\n")

# Call the main function with the username
if __name__ == "__main__":
    usernames = ["spideraxe30",'johnbummit','notnaviLoL',"weaglelol"]  # Example username, replace with actual
    
    main(usernames)
