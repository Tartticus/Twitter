def twitter_ai_response(tweet):
    
    
    xai_bearer = os.getenv("grok_api_bearer")
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {xai_bearer}"
    }
    
    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are a 62 year old lillia main"
            },
            {
                "role": "user",
                "content": f""""Respond to this like you would respond as a 62 year old 5'4 trump supporter. You are replying to the @JohnBummit, that is you. dont mention @johnbummit (limit 150 chars): {tweet}"""
            }
        ],
        "best_of": 4,
        "model": "grok-3",
        "stream": False,
        "temperature": 0,
        "top_p": 0.1,
        "temperature": 0
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    
    Test = response.json()
    
    content = Test['choices'][0]['message']['content']
    
    #niggafy
    content = content + ', nigga'
    print(f"Tweet: {tweet}")
    print(f"Grok reply: {content}")
    return content
