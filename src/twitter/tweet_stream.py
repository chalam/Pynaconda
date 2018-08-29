from __future__ import absolute_import, print_function

import yaml
from tweepy import API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from ttp import ttp
p = ttp.Parser()

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        res = p.parse(data)
        print('tweet-', data)
        print('users', res.users)
        print('tags', res.tags)
        print('html',res.html)
        print('lists',res.lists)
        print('reply',res.reply)
        print('urls', res.urls)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    cfg={}
    with open("secret_config.yml", 'r') as stream:
        try:
            cfg = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    auth = OAuthHandler(cfg['TWITTER_APP_KEY'], cfg['TWITTER_APP_SECRET'])
    auth.set_access_token(cfg['TWITTER_ACCESS_TOKEN'], cfg['TWITTER_ACCESS_TOKEN_SECRET'])

    api = API(auth)

    # If the authentication was successful, you should
    # see the name of the account print out
    print(api.me().name)
    # If the application settings are set for "Read and Write" then
    # this line should tweet out the message to your account's
    # timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
    # api.update_status(status='Hi tweeps, updating using OAuth authentication via Tweepy!')

    stream = Stream(auth, l)
    # stream.filter(track=['deep learning'])
    stream.filter(track=['trump'])