import requests
import tweepy
from datetime import datetime

def get_twitter_api():
    # Replace these with your Twitter credentials
    # Replace these with your Twitter credentials
    api_key = 'your api key'
    api_key_secret = 'your api key'
    consumer_key = 'your consumer key'
    consumer_secret = 'your consumer secret'
    access_token = ''
    access_secret = ''

    
    
    bearer_token = ''
    client = tweepy.Client(bearer_token=bearer_token, consumer_key=api_key, consumer_secret=api_key_secret, access_token=access_token, access_token_secret=access_secret)
    return client



def get_player_id(first_name, last_name, api_key):
    players_api_url = 'https://api.balldontlie.io/v1/players'
    headers = {
        'Authorization': api_key
    }
    params = {
        'search': last_name
    }
    response = requests.get(players_api_url, headers=headers, params=params)
    if response.status_code == 200:
        players = response.json()['data']
        for player in players:
            if player['first_name'].lower() == first_name.lower() and player['last_name'].lower() == last_name.lower():
                return player['id']
    return None

def get_game_stats_by_date(player_id, game_date, api_key):
    stats_api_url = 'https://api.balldontlie.io/v1/stats'
    headers = {
        'Authorization': api_key
    }
    params = {
        'player_ids[]': player_id,
        'start_date': game_date,
        'end_date': game_date
    }
    response = requests.get(stats_api_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to fetch stats')
        return None

# Main function
def main():
    twitter_api = get_twitter_api()

    # Ask user for the player's name
    first_name = input("Enter the player's first name: ")
    last_name = input("Enter the player's last name: ")

    # Ask user for their API key
    api_key = '5f596e72-b1b2-4a3f-968a-d50ac2dec97f'

    # Get player ID
    player_id = get_player_id(first_name, last_name, api_key)

    # Ask user for the game date
    user_input_date = input("Enter the game date (YYYY-MM-DD): ")
    # Validate and format the date
    try:
        game_date = datetime.strptime(user_input_date, '%Y-%m-%d').strftime('%Y-%m-%d')
    except ValueError:
        print("Incorrect date format, should be YYYY-MM-DD")
        return

    if player_id:
        game_stats = get_game_stats_by_date(player_id, game_date, api_key)
        if game_stats and game_stats['data']:
        
            latest_game = game_stats['data'][0]
            tweet = (
                f"{first_name} {last_name} on {game_date}:\n"
                f"Points: {latest_game['pts']} 🔥\n"
                f"Rebounds: {latest_game['reb']} 🔥\n"
                f"Assists: {latest_game['ast']} 🔥\n"
                "Greatest Antokounmpo of all timeT🔥"
            )
            # Post tweet using Twitter API v2
            response = twitter_api.create_tweet(text=tweet)
            if response:
                print("Tweet posted successfully!")
        else:
            print(f"No games found for {first_name} {last_name} on {game_date}.")
    else:
        print(f"{first_name} {last_name} not found.")


if __name__ == "__main__":
    main()
