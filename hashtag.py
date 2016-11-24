#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
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
import time
def get_auth():
	auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	return auth


def get_api():
	return tweepy.API(get_auth())


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

	def on_data(self, data):
		data = json.loads(data)
		text = data["text"]
		username = all_data["user"]["screen_name"]
		print ((username, text))
		time.sleep(5)
		return True


	def on_error(self, status_code):
		print "Error status_code: " + str(status_code)
		
		if status_code == 420:
			time.sleep(5)
			return True #returning False in on_error disconnects the stream
		return True



def get_stream(keyword_list, api):
	#This handles Twitter authetification and the connection to Twitter Streaming API
	l = StdOutListener()
	
	stream = Stream(api.auth, l)

	print "Streaming hashtags: " + str(keyword_list)
	#This line filter Twitter Streams to capture data by the keywords list
	stream.filter(track = keyword_list, async=True)


def search(keyword_list, api):
	#hashtag = 'IndiaAgainstCorruption'
	for hashtag in keyword_list:

		tweets = tweepy.Cursor(api.search, q = hashtag, lang='en').items(10)
		i = 0
		output_tweets = []
		with open(hashtag+'_tweets.json', 'w') as json_f:
			try:
				print "Getting Tweets"
				for tweet in tweets:
					dump = json.dumps(tweet._json)
					dump = json.loads(dump)
					output_tweets.append(dump)
					i += 1
			except Exception, e:
				print "Error: " + str(e)
			finally:
				o = {"tweets": output_tweets, "count": i}
				to_file = json.dumps(o, indent=4, separators=(',', ': '), sort_keys=True)
				json_f.write(to_file)
				print "Total Tweets: {0}".format(i)
				print "Done"


if __name__ == '__main__':
	keyword_list = []
	for word in sys.argv:
		if word[0]=='_':
			keyword_list.append('#' + word[1:])
		else:
			keyword_list.append(word)
	del keyword_list[0]

	if len(keyword_list)==0:
		print "Usage: {0} hashtag\nExample: $ python {0} IndiaAgainstCorruption _BlackMoney\nPrepend hashtags with _ (underscore)".format(sys.argv[0])
	
	else:
		api = get_api()
		print keyword_list
		get_stream(keyword_list, api)
		#search(keyword_list, api)