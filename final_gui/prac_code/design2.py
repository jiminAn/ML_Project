# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time

class TweetWidget(QtWidgets.QWidget):
    def __init__(self, time, tweet, keywords):
        QtWidgets.QWidget.__init__(self, flags=QtCore.Qt.Widget)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setStretch(1, 2)
        self.layout.setStretch(2, 1)

        self.tweet_widget_time = QtWidgets.QLabel()
        self.tweet_widget_time.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tweet_widget_time.setObjectName("tweet_widget_time")
        self.tweet_widget_time.setText(time)
        self.layout.addWidget(self.tweet_widget_time)

        self.horiz_layout = QtWidgets.QHBoxLayout()

        self.tweet_widget_tweet = QtWidgets.QLabel()
        self.tweet_widget_tweet.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tweet_widget_tweet.setObjectName("tweet_widget_tweet")
        self.tweet_widget_tweet.setText(tweet)
        self.horiz_layout.addWidget(self.tweet_widget_tweet)

        self.tweet_widget_prediction = QtWidgets.QLabel()
        self.tweet_widget_prediction.setEnabled(False)
        self.tweet_widget_prediction.setFrameShape(QtWidgets.QFrame.Box)
        self.tweet_widget_prediction.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tweet_widget_prediction.setAlignment(QtCore.Qt.AlignCenter)
        self.tweet_widget_prediction.setObjectName("tweet_widget_prediction")
        self.tweet_widget_prediction.setText("Prediction")
        self.horiz_layout.addWidget(self.tweet_widget_prediction)
        self.horiz_layout.setStretch(3, 1)

        self.layout.addLayout(self.horiz_layout)

        self.tweet_widget_keyword = QtWidgets.QLabel()
        self.tweet_widget_keyword.setAlignment(QtCore.Qt.AlignCenter)
        self.tweet_widget_keyword.setObjectName("tweet_widget_keyword")
        self.tweet_widget_keyword.setText(keywords)
        self.layout.addWidget(self.tweet_widget_keyword)

        self.setLayout(self.layout)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.keyword_line_editor = QtWidgets.QLineEdit(self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(18)
        self.keyword_line_editor.setFont(font)
        self.keyword_line_editor.setToolTipDuration(-3)
        self.keyword_line_editor.setInputMask("")
        self.keyword_line_editor.setMaxLength(32767)
        self.keyword_line_editor.setFrame(True)
        self.keyword_line_editor.setAlignment(QtCore.Qt.AlignCenter)
        self.keyword_line_editor.setDragEnabled(True)
        self.keyword_line_editor.setObjectName("keyword_line_editor")
        self.verticalLayout.addWidget(self.keyword_line_editor)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.keyword_add_btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.keyword_add2list())
        self.keyword_add_btn.setObjectName("keyword_add_btn")
        self.horizontalLayout_2.addWidget(self.keyword_add_btn)
        self.keyword_del_btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.keyword_delete())
        self.keyword_del_btn.setObjectName("keyword_del_btn")
        self.horizontalLayout_2.addWidget(self.keyword_del_btn)
        self.keyword_clear_btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.keyword_clear())
        self.keyword_clear_btn.setObjectName("keyword_clear_btn")
        self.horizontalLayout_2.addWidget(self.keyword_clear_btn)
        self.keyword_update_btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.keyword_update())
        self.keyword_update_btn.setObjectName("keyword_update_btn")
        self.horizontalLayout_2.addWidget(self.keyword_update_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.keyword_list = QtWidgets.QListWidget(self.centralwidget)
        self.keyword_list.setObjectName("keyword_list")
        self.verticalLayout.addWidget(self.keyword_list)
        self.keyword_label = QtWidgets.QLabel(self.centralwidget)
        self.keyword_label.setEnabled(False)

        font = QtGui.QFont()
        font.setPointSize(18)
        self.keyword_label.setFont(font)
        self.keyword_label.setAutoFillBackground(True)
        self.keyword_label.setFrameShape(QtWidgets.QFrame.Box)
        self.keyword_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.keyword_label.setAlignment(QtCore.Qt.AlignCenter)
        self.keyword_label.setObjectName("keyword_label")
        self.verticalLayout.addWidget(self.keyword_label)

        self.tweet_widget_list = QtWidgets.QListWidget(self.centralwidget)
        self.tweet_widget_list.setAcceptDrops(True)
        self.tweet_widget_list.setObjectName("tweet_widget_list")
        self.tweet_widget_list.setAutoScroll(True)
        self.tweet_widget_list.setLayout(QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.BottomToTop))

        self.verticalLayout.addWidget(self.tweet_widget_list)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(4, 4)
        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tweet Disaster Classifier"))
        self.keyword_add_btn.setText(_translate("MainWindow", "Add"))
        self.keyword_del_btn.setText(_translate("MainWindow", "Delete"))
        self.keyword_clear_btn.setText(_translate("MainWindow", "Clear All"))
        self.keyword_update_btn.setText(_translate("MainWindow", "Update"))
        self.keyword_label.setText(_translate("MainWindow", "keywords"))

    def add_tweet_widget(self, tweet):
        # _item = QtWidgets.QListWidgetItem(self.tweet_widget_list)
        # _item.setSizeHint(tweet.sizeHint())
        #
        # self.tweet_widget_list.insertItem(0, _item)
        # self.tweet_widget_list.setItemWidget(_item, tweet)
        #
        # self.tweet_widget_list.insertItem(0, time.ctime())

        item = QtWidgets.QListWidgetItem(self.tweet_widget_list)
        item.setText(time.ctime())

        self.tweet_widget_list.insertItem(0, item)


    def keyword_add2list(self):
        keyword = self.keyword_line_editor.text()

        if keyword != "":
            self.keyword_list.addItem(keyword)
        self.keyword_line_editor.setText("")

    def keyword_delete(self):
        keyword_cur_row = self.keyword_list.currentRow()
        print(self.tweet_widget_list.currentRow())
        self.keyword_list.takeItem(keyword_cur_row)

    def keyword_clear(self):
        self.keyword_list.clear()

    def keyword_update(self):
        keywords = [self.keyword_list.item(i) for i in range(self.keyword_list.count())]
        self.keyword_label.setText(" ".join(["#" + kw.text() for kw in keywords]))

        self.add_tweet_widget(
            TweetWidget(time.ctime(),
                      "Unix ?????????????????? ????????? ????????? ????????? ??????????????? ????????? ?????? ????????????(command interpreter)",
                      self.keyword_label.text()
            )
        )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

