from PyQt5 import QtCore, QtGui, QtWidgets

import backend
from results_window import Ui_ResultsWindow


class Ui_GuessWindow(object):
    def openWindow(self):
        backend.song_guess += self.box01_text() + self.box02_text() + self.box03_text()

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ResultsWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, GuessWindow):
        GuessWindow.setObjectName("GuessWindow")
        GuessWindow.resize(737, 604)
        GuessWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(GuessWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 1, 801, 131))
        self.label.setStyleSheet("image: url(:/newPrefix/billboard_hot_100.png);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 160, 801, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 240, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 300, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 360, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton.setGeometry(QtCore.QRect(300, 510, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(162, 162, 167);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.pushButton.setObjectName("pushButton")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 460, 81, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.editingFinished.connect(self.box01_text)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 430, 81, 21))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 460, 81, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.editingFinished.connect(self.box02_text)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 430, 81, 21))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 460, 81, 21))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.editingFinished.connect(self.box03_text)

        GuessWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GuessWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 24))
        self.menubar.setObjectName("menubar")
        GuessWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(GuessWindow)
        self.statusbar.setObjectName("statusbar")
        GuessWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GuessWindow)
        QtCore.QMetaObject.connectSlotsByName(GuessWindow)

    def retranslateUi(self, GuessWindow):
        _translate = QtCore.QCoreApplication.translate
        GuessWindow.setWindowTitle(_translate("GuessWindow", "MainWindow"))

        self.label_2.setText(_translate("GuessWindow", "Here are your songs to order!"))
        self.label_3.setText(_translate("GuessWindow", backend.print_songs(backend.songs, 0)))
        self.label_4.setText(_translate("GuessWindow", backend.print_songs(backend.songs, 1)))
        self.label_5.setText(_translate("GuessWindow", backend.print_songs(backend.songs, 2)))
        self.pushButton.setText(_translate("GuessWindow", "Submit!"))
        self.label_6.setText(_translate("GuessWindow", "Highest:"))
        self.label_8.setText(_translate("GuessWindow", "Lowest"))

    def box01_text(self):
        return self.lineEdit.text()

    def box02_text(self):
        return self.lineEdit_2.text()

    def box03_text(self):
        return self.lineEdit_3.text()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    GuessWindow = QtWidgets.QMainWindow()
    ui = Ui_GuessWindow()
    ui.setupUi(GuessWindow)
    GuessWindow.show()

    sys.exit(app.exec_())
