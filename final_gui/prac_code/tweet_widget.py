# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tweet_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TweetWidget(object):
    def setupUi(self, TweetWidget):
        TweetWidget.setObjectName("TweetWidget")
        TweetWidget.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(TweetWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 371, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tweet_widget_time = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.tweet_widget_time.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tweet_widget_time.setObjectName("tweet_widget_time")
        self.verticalLayout.addWidget(self.tweet_widget_time)
        self.tweet_widget_tweet = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.tweet_widget_tweet.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tweet_widget_tweet.setObjectName("tweet_widget_tweet")
        self.verticalLayout.addWidget(self.tweet_widget_tweet)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tweet_widget_keyword = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.tweet_widget_keyword.setAlignment(QtCore.Qt.AlignCenter)
        self.tweet_widget_keyword.setObjectName("tweet_widget_keyword")
        self.horizontalLayout.addWidget(self.tweet_widget_keyword)
        self.tweet_widget_prediction = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.tweet_widget_prediction.setEnabled(False)
        self.tweet_widget_prediction.setFrameShape(QtWidgets.QFrame.Box)
        self.tweet_widget_prediction.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tweet_widget_prediction.setAlignment(QtCore.Qt.AlignCenter)
        self.tweet_widget_prediction.setObjectName("tweet_widget_prediction")
        self.horizontalLayout.addWidget(self.tweet_widget_prediction)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(TweetWidget)
        QtCore.QMetaObject.connectSlotsByName(TweetWidget)


    def retranslateUi(self, TweetWidget):
        _translate = QtCore.QCoreApplication.translate
        TweetWidget.setWindowTitle(_translate("TweetWidget", "Form"))
        self.tweet_widget_time.setText(_translate("TweetWidget", "time"))
        self.tweet_widget_tweet.setText(_translate("TweetWidget", "tweet"))
        self.tweet_widget_keyword.setText(_translate("TweetWidget", "keywords"))
        self.tweet_widget_prediction.setText(_translate("TweetWidget", "label"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TweetWidget = QtWidgets.QWidget()
    ui = Ui_TweetWidget()
    ui.setupUi(TweetWidget)
    TweetWidget.show()
    sys.exit(app.exec_())

