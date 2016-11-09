#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

from SentimentAnalysisModule import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
import sys, getopt
from urllib import quote, urlencode
from urllib import urlretrieve

import requests
import base64
import json

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

	def on_data(self, data):
		print data
		return True

	def on_error(self, status):
		print "Error status: " + str(status)


def get_auth():
	auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	return auth


def get_api():
	return tweepy.API(get_auth())


def get_stream(keyword_list = None):
	#This handles Twitter authetification and the connection to Twitter Streaming API
	l = StdOutListener()
	auth = get_auth()
	stream = Stream(auth, l)

	print "Streaming keywords: " + str(keyword_list)
	#This line filter Twitter Streams to capture data by the keywords list
	stream.filter(track=keyword_list)


def search(hashtag):
	api = get_api()
	#hashtag = 'IndiaAgainstCorruption'
	tweets = tweepy.Cursor(api.search, q='#'+hashtag).items(10)
	i = 0
	output_tweets = []
	with open(hashtag+'_tweets.json', 'w') as json_f:
		try:
			print "Getting Tweets"
			for tweet in tweets:
				dump = json.dumps(tweet._json)
				dump = json.loads(dump)
				output_tweets.append(dump)
				i+=1
		except Exception, e:
			print "Error: " + str(e)
		finally:
			o = {"tweets": output_tweets, "count": i}
			to_file = json.dumps(o, indent=4, separators=(',', ': '), sort_keys=True)
			json_f.write(to_file)
			print "Total Tweets: {0}".format(i)
			print "Done"


if __name__ == '__main__':
	kw_list = []
	for word in sys.argv:
		kw_list.append(word)
	del kw_list[0]

	if len(kw_list)==0:
		print "Usage: {0} hashtag\nExample: $ python {0} IndiaAgainstCorruption".format(sys.argv[0])
	
	else:
		#get_stream(kw_list)
		search(kw_list[0])