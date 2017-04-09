# TwitterDataAnalysis


## Authentication
In order to access Twitter APIs, we need to get 4 pieces of information from Twitter: API key, API secret, Access token and Access token secret. Follow the steps below to get all 4 elements:

1. Create a twitter account if you do not already have one.
2. Go to https://apps.twitter.com/ and log in with your twitter credentials.
3. Click "Create New App"
4. Fill out the form, agree to the terms, and click "Create your Twitter application"
5. In the next page, click on "API keys" tab, and copy your "API key" and "API secret".
6. Scroll down and click "Create my access token", and copy your "Access token" and "Access token secret".
7. Now store these values in API_DATA.py file in SentimentAnalysisModule folder.(Format given in sample file)


## Run
1. Run the script _indiaagainstcorruption.py_ using the command.  
	`$ python hashtag.py search_term _hashtag`
Note: append '_' with a hashtag you want to search for.

2. See the output in `hashtag`_tweet.json
