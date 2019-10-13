import twitter

api = twitter.Api(
    consumer_key='XXXXXXXXXXXXXXXXXXXXX',
    consumer_secret='XXXXXXXXXXXXXXXXXXXXX',
    access_token_key='XXXXXXXXXXXXXXXXXXXXX',
    access_token_secret='XXXXXXXXXXXXXXXXXXXXX')

result = api.VerifyCredentials()

print(result)

new_tweets = api.GetUserTimeline(screen_name='Inderpreet Jhajj', count=200)
for tweet in new_tweets:
    print(tweet.text)
