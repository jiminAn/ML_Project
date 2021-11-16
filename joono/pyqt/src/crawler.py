import os
import twitter
import json

from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

class TweetStream(QThread):
    takeTweetSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.twitter_consumer_key = "..."
        self.twitter_consumer_secret = "..."
        self.twitter_access_token = "...-..."
        self.twitter_access_secret = "..."

        self.keywords = ["lol", "faker"]

        self.twitter_api = twitter.Api(consumer_key=self.twitter_consumer_key,
                                       consumer_secret=self.twitter_consumer_secret,
                                       access_token_key=self.twitter_access_token,
                                       access_token_secret=self.twitter_access_secret)

        self.isRdy = False

    def run(self) -> None:
        # act like semaphore
        while not self.isRdy:
            pass

        while True:
            if self.isRdy:
                try:
                    self.sleep(2)

                    stream = self.twitter_api.GetStreamFilter(track=self.keywords)
                    for tweets in stream:
                        self.takeTweetSignal.emit(str(tweets['text']))
                except Exception as e:
                    print(e)
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
        # act like semaphore
        while not self.isRdy:
            pass

        while True:
            if self.isRdy:
                with open(self.testDsetPath, "r") as f:
                    for tweet_csv in f.readlines():
                        try:
                            tweet = tweet_csv.split(",")[2]
                            self.takeTweetSignal.emit(tweet)
                        except:
                            pass


                        self.msleep(500)
            else:
                break

    def terminate(self) -> None:
        self.isRdy = False

    def updateKeywords(self, keywords):
        self.keywords = keywords
