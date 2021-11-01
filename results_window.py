from PyQt5 import QtCore, QtGui, QtWidgets
import backend


class Ui_ResultsWindow(object):
    def setupUi(self, ResultsWindow):
        ResultsWindow.setObjectName("ResultsWindow")
        ResultsWindow.resize(800, 600)
        ResultsWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(ResultsWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 1, 801, 131))
        self.label.setStyleSheet("image: url(:/newPrefix/billboard_hot_100.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        if backend.song_guess == backend.song_order:
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(0, 150, 801, 61))
            font = QtGui.QFont()
            font.setFamily("Arial Rounded MT Bold")
            font.setPointSize(72)
            self.label_2.setFont(font)
            self.label_2.setStyleSheet("color: rgb(0, 255, 0);")
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
            self.label_2.setObjectName("label_2")

        else:
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(0, 150, 801, 61))
            font = QtGui.QFont()
            font.setFamily("Arial Rounded MT Bold")
            font.setPointSize(72)
            self.label_3.setFont(font)
            self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
            self.label_3.setAlignment(QtCore.Qt.AlignCenter)
            self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 240, 801, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 280, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 330, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 380, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 450, 801, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        ResultsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ResultsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        ResultsWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(ResultsWindow)
        self.statusbar.setObjectName("statusbar")
        ResultsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultsWindow)

    def retranslateUi(self, ResultsWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultsWindow.setWindowTitle(_translate("ResultsWindow", "MainWindow"))

        if backend.song_guess == backend.song_order:
            self.label_2.setText(_translate("ResultsWindow", "CORRECT!"))
        else:
            self.label_3.setText(_translate("ResultsWindow", "Incorrect."))

        self.label_4.setText(_translate("ResultsWindow", "Here is the correct list order! ({})".format(backend.song_order)))
        self.label_5.setText(_translate("ResultsWindow",
                                        backend.print_songs_numbered(backend.reorder_songs(backend.songs,
                                                                                           backend.num_songs), 0)))
        self.label_6.setText(_translate("ResultsWindow",
                                        backend.print_songs_numbered(backend.reorder_songs(backend.songs,
                                                                                           backend.num_songs), 1)))
        self.label_7.setText(_translate("ResultsWindow",
                                        backend.print_songs_numbered(backend.reorder_songs(backend.songs,
                                                                                           backend.num_songs), 2)))
        self.label_8.setText(_translate("ResultsWindow", "Thanks for playing!!"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ResultsWindow = QtWidgets.QMainWindow()
    ui = Ui_ResultsWindow()
    ui.setupUi(ResultsWindow)
    ResultsWindow.show()

    sys.exit(app.exec_())
