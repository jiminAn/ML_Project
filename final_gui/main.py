from PyQt5 import QtWidgets

import sys
import src.ui as ui
import src.crawler as crawler
import src.tweet_model as tweet_model


if __name__ == "__main__":

    model = tweet_model.DisasterModel()
    crawler = crawler.TestTweetStream()
    ui = ui.Ui_MainWindow(crawler)

    crawler.takeTweetSignal.connect(model.prediction)
    model.predictionDone.connect(ui.add_tweet_widget)

    crawler.start()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())