# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.keyword_line_editor.setMaxLength(20)
        self.keyword_line_editor.setFrame(True)
        self.keyword_line_editor.setAlignment(QtCore.Qt.AlignCenter)
        self.keyword_line_editor.setDragEnabled(True)
        self.keyword_line_editor.setObjectName("keyword_line_editor")
        self.verticalLayout.addWidget(self.keyword_line_editor)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.keyword_add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.keyword_add_btn.setObjectName("keyword_add_btn")
        self.horizontalLayout_2.addWidget(self.keyword_add_btn)
        self.keyword_del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.keyword_del_btn.setObjectName("keyword_del_btn")
        self.horizontalLayout_2.addWidget(self.keyword_del_btn)
        self.keyword_clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.keyword_clear_btn.setObjectName("keyword_clear_btn")
        self.horizontalLayout_2.addWidget(self.keyword_clear_btn)
        self.keyword_update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.keyword_update_btn.setObjectName("keyword_update_btn")
        self.horizontalLayout_2.addWidget(self.keyword_update_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.realtime_tweet_predictions = QtWidgets.QScrollArea(self.centralwidget)
        self.realtime_tweet_predictions.setFrameShape(QtWidgets.QFrame.Box)
        self.realtime_tweet_predictions.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.realtime_tweet_predictions.setWidgetResizable(True)
        self.realtime_tweet_predictions.setAlignment(QtCore.Qt.AlignCenter)
        self.realtime_tweet_predictions.setObjectName("realtime_tweet_predictions")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 690, 441))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.realtime_tweet_predictions.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.realtime_tweet_predictions)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 4)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.keyword_line_editor.setInputMask(_translate("MainWindow", "Please enter keyword"))
        self.keyword_add_btn.setText(_translate("MainWindow", "Add"))
        self.keyword_del_btn.setText(_translate("MainWindow", "Delete"))
        self.keyword_clear_btn.setText(_translate("MainWindow", "Clear All"))
        self.keyword_update_btn.setText(_translate("MainWindow", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

