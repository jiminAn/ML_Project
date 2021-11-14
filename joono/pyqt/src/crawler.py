import os
import twitter
import json

from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from src.tweet_model import DisasterModel

class TweetStream(QThread):
    takeTweetSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.twitter_consumer_key = ""
        self.twitter_consumer_secret = ""
        self.twitter_access_token = ""
        self.twitter_access_secret = ""

        self.keywords = ["#larva"]

        self.twitter_api = twitter.Api(consumer_key=self.twitter_consumer_key,
                                       consumer_secret=self.twitter_consumer_secret,
                                       access_token_key=self.twitter_access_token,
                                       access_token_secret=self.twitter_access_secret)

        self.stream = self.twitter_api.GetStreamFilter(track=self.keywords)
        self.isRdy = False

    def run(self) -> None:
        while True:
            if self.isRdy:
                for tweets in self.stream:
                    tweet = json.dumps(tweets, ensure_ascii=False)
                    print(tweet)
                    self.takeTweetSignal.emit(str(tweet['text']))
            else:
                break

    def terminate(self) -> None:
        self.isRdy = False

    def updateKeywords(self, keywords):
        self.keywords = keywords

class TestTweetStream(QThread):
    takeTweetSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.keywords = ["#larva"]
        self.isRdy = False
        self.testDsetPath = os.path.join("src", "data", "origin_test.csv")

    def run(self) -> None:
        self.isRdy = True

        while True:
            if self.isRdy:
                with open(self.testDsetPath, "r") as f:
                    for tweet_csv in f.readlines():
                        try:
                            tweet = tweet_csv.split(",")[2]
                            self.takeTweetSignal.emit(tweet)
                        except:
                            pass


                        self.msleep(1500)
            else:
                break

    def terminate(self) -> None:
        self.isRdy = False

    def updateKeywords(self, keywords):
        self.keywords = keywords