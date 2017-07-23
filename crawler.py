import twitter
import re
import html

def get_twitter_user(username):

    api = twitter.Api(consumer_key='qqyWrUQicjEmbSaKM7I4enicg',
                      consumer_secret='l9mEz08T7jAPRMpjx3uOC9r5NTFwv486dfqrC86mlE4KUdsNld',
                      access_token_key='845935402359799812-oxG2qO7b8BArh4svMUsjj93ptaymelK',
                      access_token_secret='0nFvziZd84tvxmyYjEQsrRtxMWKNjPuihMyLkzmZi7aVF',
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