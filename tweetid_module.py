from requests_oauthlib import OAuth1Session
import json


def get_tweetID(CK, CS, AT, AS, ID):

    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

    params = {"user_id": ID, "count": 1}

    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.get(url, params=params)

    if req.status_code == 200:

        timeline = json.loads(req.text)

        for tweet in timeline:
            return tweet["id"]

    else:
        # エラーの場合
        print("Error: %d" % req.status_code)


if __name__ == "__main__":

    print(tweetID(CK, CS, AT, AS, ID))