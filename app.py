import config
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream

class MyListener(StreamListener):
    def on_data(self, data):
        try:
             with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

if __name__ == "__main__":
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)

    api = tweepy.API(auth)

    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter(track=['#Betis'])

    print("alright!")
