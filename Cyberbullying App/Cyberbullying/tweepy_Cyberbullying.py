import pandas as pd
import tweepy
from tweepy import OAuthHandler


class Import_tweet_Cyberbullying:

	consumer_key="ijblQaazlKXFz4wJ4dH22ORI8"
	consumer_secret="ovjp3m4SVawtuKHjpUvcEEAR2ynsrxmB24OTHdsBsA5vN2hqk3"
	access_token="1409807449209589761-WXFpVOL3ZY0XDt1gC0Em8PvJmEYdNy"
	access_token_secret="F6DLLfWsQXbIAot7og4PJY7bT8fpn7gQECV9jI3JcJV3T"

	def tweet_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		return df

	def get_tweets(self, handle):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		#auth_api = API(auth)
		auth_api= tweepy.API(auth, wait_on_rate_limit=True)

		account = handle
		item = auth_api.user_timeline(id=account,count=20)
		df = self.tweet_to_data_frame(item)

		all_tweets = []
		for j in range(20):
			all_tweets.append(df.loc[j]['Tweets'])
		return all_tweets

	def get_hashtag(self, hashtag):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = tweepy.API(auth, wait_on_rate_limit=True)
		#auth_api = API(auth)

		account = hashtag
		all_tweets = []

		for tweet in tweepy.Cursor(auth_api.search_tweets, q=account, lang='en').items(20):
			all_tweets.append(tweet.text)

		return all_tweets
