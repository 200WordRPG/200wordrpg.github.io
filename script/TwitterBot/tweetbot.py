import tweepy
import json
import urllib
import random
import time

# Simple script to scan the 200WordRPG allposts.json file and tweet a random entry.
# Deployed to heroku, runs once a day. 
# Used this tutorial: https://briancaffey.github.io/2016/04/05/twitter-bot-tutorial.html

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
me = api.me()

# set the default entry
randomEntry = {"title" : "test","href" : "test","author" : "David Schirduan"}

# picks a random entry from the allposts.json
def pickRandomEntry(randE):

    url = urllib.urlopen("https://200wordrpg.github.io/allposts.json")
    data = json.loads(url.read())
    
    num = random.randrange(0, len(data))
    randE = data[num]
    return randE

# runs until a random entry that ISN'T news or kintsugi
def tweetOut(randomE):
    while (randomE['author'] == "David Schirduan"):
        randomE = pickRandomEntry(randomE)

    twit = '"' + randomE['title'] + "\" by " + randomE['author'] + " \nis the 200 Word RPG of the Day! \nhttps://200wordrpg.github.io" + randomE['href']

    print(twit)
    api.update_status(twit.encode('utf-8').strip())

#Auto-follow new followers
#for follower in tweepy.Cursor(api.followers, id = me.id, count = 190).items():
#    try:
#        follower.follow()
#    except tweepy.error.TweepError:
#        pass
	
# runs once a day from Heroku servers
tweetOut(randomEntry)
