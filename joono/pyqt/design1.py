# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 681, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tweet_editor = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.tweet_editor.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.tweet_editor.setFont(font)
        self.tweet_editor.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tweet_editor.setAutoFillBackground(True)
        self.tweet_editor.setFrameShape(QtWidgets.QFrame.Box)
        self.tweet_editor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tweet_editor.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tweet_editor.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tweet_editor.setObjectName("tweet_editor")
        self.verticalLayout.addWidget(self.tweet_editor)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.answer_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.answer_label.setFrameShape(QtWidgets.QFrame.Box)
        self.answer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_label.setObjectName("answer_label")
        self.horizontalLayout.addWidget(self.answer_label)
        self.predict_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.predict_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.predict_btn.setObjectName("predict_btn")
        self.horizontalLayout.addWidget(self.predict_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
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
        self.tweet_editor.setDocumentTitle(_translate("MainWindow", "tweet"))
        self.answer_label.setText(_translate("MainWindow", "Answer"))
        self.predict_btn.setText(_translate("MainWindow", "Predict"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

