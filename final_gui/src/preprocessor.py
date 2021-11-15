import re
import string



class TweetPreprocessor:

    def preprocessing(self, tweet):
        tweet = {"origin": tweet, 'processed': tweet}

        tweet["processed"] = self.remove_URL(tweet["processed"])
        tweet["processed"] = self.remove_html(tweet["processed"])
        tweet["processed"] = self.remove_punct(tweet["processed"])
        tweet["processed"] = self.clean_text(tweet["processed"])

        return tweet

    def remove_URL(self, text):  # remove url pattern in text
        url = re.compile(r'https?://\S+|www\.\S+')
        return url.sub(r'', text)

    def remove_html(self, text):  # remove html pattern in text
        html = re.compile(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        return html.sub(r'', text)

    def remove_punct(self, text):  # remove punctuation in text: (;, ', ", :, ., , etc..)
        table = str.maketrans('', '', string.punctuation)
        return text.translate(table)

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"i'm", "i am", text)
        text = re.sub(r"you'll", "you will", text)
        text = re.sub(r"i'll", "i will", text)
        text = re.sub(r"she'll", "she will", text)
        text = re.sub(r"he'll", "he will", text)
        text = re.sub(r"he's", "he is", text)
        text = re.sub(r"she's", "she is", text)
        text = re.sub(r"that's", "that is", text)
        text = re.sub(r"what's", "what is", text)
        text = re.sub(r"where's", "where is", text)
        text = re.sub(r"there's", "there is", text)
        text = re.sub(r"here's", "here is", text)
        text = re.sub(r"who's", "who is", text)
        text = re.sub(r"how's", "how is", text)
        text = re.sub(r"\'ll", " will", text)
        text = re.sub(r"\'ve", " have", text)
        text = re.sub(r"\'re", " are", text)
        text = re.sub(r"\'d", " would", text)
        text = re.sub(r"can't", "cannot", text)
        text = re.sub(r"won't", "will not", text)
        text = re.sub(r"don't", "do not", text)
        text = re.sub(r"shouldn't", "should not", text)
        text = re.sub(r"n't", " not", text)
        text = re.sub(r"   ", " ", text)  # Remove any extra spaces

        return text

