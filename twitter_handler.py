import twitter
import csv
import re
import os
from celery import Celery
import time
from celery.decorators import periodic_task
from datetime import timedelta



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#os.path.abspath(__file__) = /Users/tarungupta/Documents/Django/DjangoScrapy/Social-Ingestor/twitter_handler.py
#os.path.dirname(os.path.abspath(__file__)) = /Users/tarungupta/Documents/Django/DjangoScrapy/Social-Ingestor


api = twitter.Api(
    consumer_key='3K6rpyPp7uqbOdKsprC3KJJKR',
    consumer_secret='kSmjcUuYWjFfvyy7MpVXUUCfnyKo2ioQWqLbmUfLZxEr534RaD',
    access_token_key='1182561318823284737-hCNzDdhMA8PzCnlpFky7fl4uNn4ZHD',
    access_token_secret='ZlF2dyk4KHaxnMZKSK0b1AlgRrJmaJRPahKsNjrAI0se7')

app = Celery('twitter_handler', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

@periodic_task(run_every=timedelta(seconds=10), name='tasks.get_all_tweets')
def get_all_tweets():
#def get_all_tweets(screen_name):
    print(api.VerifyCredentials())
    screen_name = 'Inderpreet Jhajj'
    allTweets = []
    new_tweets = api.GetUserTimeline(screen_name=screen_name, count=200)
    allTweets.extend(new_tweets)

    #Oldest Tweet retrieved the last time we made the call
    oldest_tweet = allTweets[-1].id - 1
    #On subsequent calls we will be picking the tweets which are older that is with the lesser id number
    while(len(new_tweets)>0):
        print('getting tweets before {}'.format(oldest_tweet))
        new_tweets = api.GetUserTimeline(screen_name=screen_name, count=200, max_id=oldest_tweet)
        allTweets.extend(new_tweets)
        oldest_tweet = allTweets[-1].id - 1
        print('....{} tweets downloaded so far'.format(len(allTweets)))

    #delete the retweets
    cleaned_text = [re.sub(r'RT.*','', i.text, flags=re.MULTILINE) for i in allTweets]

    #delete the @twitter mentions
    cleaned_text = [re.sub(r'@[\W]*', '', i, flags=re.MULTILINE) for i in cleaned_text]

    #transform the tweets into a 2D array that will populate the csv
    out_tweets = [[tweet.id_str, tweet.created_at, cleaned_text[idx].encode('utf-8').decode('utf-8')] for idx, tweet in enumerate(allTweets)]

    with open(os.path.join(BASE_DIR, 'data','raw','{}_tweets.csv'.format(screen_name)),'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'created_at', 'text'])
        writer.writerows(out_tweets)

#if __name__=='__main__':
#    print(api.VerifyCredentials())
#    screen_name = 'Inderpreet Jhajj'
#    get_all_tweets(screen_name=screen_name)
#    print(os.path.join(BASE_DIR, 'data','raw'))
