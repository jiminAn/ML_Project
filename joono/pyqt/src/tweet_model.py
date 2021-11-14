from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject

import numpy as np
import pickle
import warnings
warnings.filterwarnings(action='ignore')  # default = off


class DisasterModel(QObject):
    predictionDone = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()

        self.model_path = "./src/weights/"
        self.loaded_vector = pickle.load(open(self.model_path+"vector002-2021-11-13-09-F1-077018.pkl", "rb"))
        self.loaded_model = pickle.load(open(self.model_path+"model002-2021-11-13-09-F1-077018.pkl", "rb"))

    @pyqtSlot(str)
    def prediction(self, tweet):
        X_test_vector = self.loaded_vector.transform([tweet])  # Generate TFIDF vector
        res = self.loaded_model.predict(X_test_vector.todense()) # input is string

        res = "Disaster" if res == 1 else "Not Disaster"

        self.predictionDone.emit(tweet, res)

if __name__ == '__main__':
    model = DisasterModel()

    model.prediction("It's raining")
    model.prediction("There's a fire over there. it's dangerous..")

