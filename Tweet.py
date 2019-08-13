import tweepy
import GenerateQuote
import tokens

consumer_token = tokens.consumer_token
consumer_secret = tokens.consumer_secret
access_token = tokens.access_token
access_secret = tokens.access_secret

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class API:

	def TweetQuote(self,manualQuote=False):
		if(manualQuote):
			quote = input("Enter quote to tweet: \n")
		else:
			q = GenerateQuote.Quote()
			quote = q.quote

		api.update_status(status=quote,lat = 41.4090, long=75.6624)

	def Retweet(self,ID):
		api.retweet(ID)

	def FollowFollowers():
		return None


if __name__ == '__main__':
	tweet = API()
	tweet.TweetQuote()