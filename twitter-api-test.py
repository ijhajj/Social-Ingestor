import twitter

api = twitter.Api(
    consumer_key='3K6rpyPp7uqbOdKsprC3KJJKR',
    consumer_secret='kSmjcUuYWjFfvyy7MpVXUUCfnyKo2ioQWqLbmUfLZxEr534RaD',
    access_token_key='1182561318823284737-hCNzDdhMA8PzCnlpFky7fl4uNn4ZHD',
    access_token_secret='ZlF2dyk4KHaxnMZKSK0b1AlgRrJmaJRPahKsNjrAI0se7')

result = api.VerifyCredentials()

print(result)

new_tweets = api.GetUserTimeline(screen_name='Inderpreet Jhajj', count=200)
for tweet in new_tweets:
    print(tweet.text)
