import twitter
import re
import html

def get_twitter_user(username):

    api = twitter.Api(consumer_key='consumer_key',
                      consumer_secret='consumer_secret',
                      access_token_key='access_token_key',
                      access_token_secret='access_token_secret',
                  tweet_mode='extended')

    # print(api.VerifyCredentials())
    statuses = api.GetUserTimeline(screen_name=username)
    results = []
    for s in statuses:
        if s.retweeted_status:
            tweet = re.sub(r"http\S+", "", s.retweeted_status.full_text)
            results.append(html.unescape(tweet.strip()))
        else:
            tweet = re.sub(r"http\S+", "", s.full_text)
            results.append(html.unescape(tweet.strip()))
    return results
