from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chooseDepth(object):
    def setupUi(self, chooseDepth):
        chooseDepth.setObjectName("chooseDepth")
        chooseDepth.resize(288, 102)
        self.centralwidget = QtWidgets.QWidget(chooseDepth)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(80, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        chooseDepth.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(chooseDepth)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 288, 21))
        self.menubar.setObjectName("menubar")
        chooseDepth.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(chooseDepth)
        self.statusbar.setObjectName("statusbar")
        chooseDepth.setStatusBar(self.statusbar)

        self.retranslateUi(chooseDepth)
        QtCore.QMetaObject.connectSlotsByName(chooseDepth)

    def retranslateUi(self, chooseDepth):
        _translate = QtCore.QCoreApplication.translate
        chooseDepth.setWindowTitle(_translate("chooseDepth", "Choose your depth"))
        self.label.setText(_translate("chooseDepth", "Depth"))
        self.pushButton.setText(_translate("chooseDepth", "Confirm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    chooseDepth = QtWidgets.QMainWindow()
    ui = Ui_chooseDepth()
    ui.setupUi(chooseDepth)
    chooseDepth.show()
    sys.exit(app.exec_())
