import tweepy
import GenerateQuote


consumer_token = 'wSLVH66l6dT8QEwnY52bP3qhz'
consumer_secret = 'dAV884TnfGLjeRdqSfMlwRFsyJvQ8rrVid3Gb1jnwDKU7JMLxX'
access_token = '1160773516540727296-ulSUTI9kKXRYlPJ54yhW19xU0k9aDL'
access_secret = 'y7bADITDoukX0xd3UJz9dyGGm4aOsMBdXmXzCKewfCeNW'

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