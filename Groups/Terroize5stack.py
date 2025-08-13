import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import requests
import re



#make sure to get your cookies
def twitter_login():
    # Open X
    driver.get("https://x.com/")
    # Step 1: Define your cookies from the browser
    cookies = [
    {   # Donald Trump simp
        "name": "auth_token",
        "value": "c0d7d59107669c906794ff0301a28839eeca9667",
        "domain": ".x.com"
    },
    {   # Jacuzzi Smith
        "name": "auth_token",
        "value": "c125edfe25a1a4b7b2ab3b6842aeb7f89d087882",
        "domain": ".x.com"
    },
    {   # Homeless Man
        "name": "auth_token",
        "value": "c125edfe25a1a4b7b2ab3b6842aeb7f89d087882",
        "domain": ".x.com"
    },
    {   # Black
        "name": "auth_token",
        "value": "c125edfe25a1a4b7b2ab3b6842aeb7f89d087882",
        "domain": ".x.com"
    },
    {   # Blackinter69
        "name": "auth_token",
        "value": "c0d7d59107669c906794ff0301a28839eeca9667",
        "domain": ".x.com"
    }
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
    time.sleep(5)
    
    
    # Get the text of the top tweet
    top_tweet2 = driver.find_element(By.XPATH, '//div[@data-testid="tweetText"]//span').text
    top_tweet = driver.find_element(By.XPATH, '(//article[@data-testid="tweet"])[2]//div[@data-testid="tweetText"]').text
    
    
    tweet = top_tweet
    return tweet



def twitter_ai_response(tweet):
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer xai-a"
    }
    
    data = {
        "messages": [
            {
            "role": "system",
            "content": "You are a Trump Supporter on twitter aged 62 thats kinda mad"
            },
            {
            "role": "user",
             "content": f"Respond to this like you would respond to a tweet kinda angrily and crazy.  bring up Epstein, and LuLu nerfs 150 characters max: {tweet}"
            }
        ],
        "best_of": 4,
        "model": "grok-4-latest",
        "stream": False,
        "temperature": 0,
        "top_p": 0.1,
        "temperature": 0
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    Test = response.json()
    
    content = Test['choices'][0]['message']['content']
    
    
    return content

def tweet_reply(response):
    
    tweet = driver.find_element(By.XPATH, '(//article[@data-testid="tweet"])[2]//div[@data-testid="tweetText"]')  # Select the second tweet to avoid pinned tweet
    tweet.click()
    
    # Step 9: Wait for the tweet to load 
    time.sleep(3)
    
    #repply field
    reply_box = driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
    # Scroll the reply box into view
    driver.execute_script("arguments[0].scrollIntoView();", reply_box)
    #function to remove emojis (not supported by selenium)
    def remove_non_bmp_characters(text):
        return re.sub(r'[^\u0000-\uFFFF]', '', text)
    response = remove_non_bmp_characters(response)
    # Step 11: Type your reply
    reply_text = response
    
    reply_box.send_keys(reply_text)
   

    
    # Step 2: Now look for and click the "Reply button" using `data-testid="tweetButtonInline"`
    reply_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@data-testid='tweetButtonInline']"))
    )
    
    driver.execute_script("arguments[0].click();", reply_button)

    # Optionally, wait a few seconds to observe the result before closing the browser
    WebDriverWait(driver, 5)
   
    
    time.sleep(5)
    return
    

# List to store the tweets we have replied to

replied_tweets_dict = {}
chrome_options = Options()
headless =  input("Would you like to start in headless mode?: 1 for yes, 2 for no\n")
if headless == '1':
    chrome_options.add_argument("--headless") 
chrome_options.add_argument("--window-size=1920,1080") 
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)
def main(usernames):
    

    # Login to twitter (put cookies here)
    twitter_login()
    # Keep running this to check for new tweets and reply
    while True:
        for username in usernames:
            print(f"processing {username}\n")
            URL = f"https://x.com/{username}"
            try:
            # Search for the top tweet from the user
                tweet = twitter_search(URL)
            except Exception() as e:
                print(e)
                continue
            # Check if we already replied to this tweet
            # Initialize the list of replied tweets for the user if not done already
            if username not in replied_tweets_dict:
                replied_tweets_dict[username] = []
        
            # Check if we already replied to this tweet2
            
            if tweet in replied_tweets_dict[username]:
                print(f"Already replied to the tweet for {username}. Waiting for a new one...")
                print("-----------------------------------------------------\n")
            else:
                print(f"Most Recent tweet from {username}: {tweet}\n")
                
                # Get an AI-generated response for the tweet
                response = twitter_ai_response(tweet)
                print(f"AI Response:{response}\n")
                
                try: # Reply to the tweet
                    tweet_reply(response)
        
                   # Add the tweet to the list of replied tweets for this account
                    replied_tweets_dict[username].append(tweet)
                    print(f"\nReply posted for {username}\n")
                    print("-----------------------------------------------------\n")
                except Exception as e:
                    print(e)
                    continue
                    
            # Wait 30 sec before checking again
            time.sleep(5)

# Call the main function with the username
if __name__ == "__main__":
    usernames = ["elonmusk","jdVANCE","RealCandaceO"]  # Example username, replace with actual
    main(usernames)
