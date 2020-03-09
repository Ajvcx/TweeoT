from requests_oauthlib import OAuth1Session
import json


def usertimeline(CK, CS, AT, AS, ID, since_id):

    tweet_list = []

    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

    params = {"user_id": ID, "count": 200, "since_id": since_id}

    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.get(url, params=params)

    if req.status_code == 200:

        timeline = json.loads(req.text)

        for tweet in timeline:
            tweet_list.append(tweet["text"])
    else:
        # エラーの場合
        print("Error: %d" % req.status_code)

    return tweet_list


if __name__ == "__main__":

    print(usertimeline(CK, CS, AT, AS, ID, since_id))
