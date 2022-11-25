from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddNodePage(object):
    def setupUi(self, AddNodePage):
        AddNodePage.setObjectName("AddNodePage")
        AddNodePage.resize(252, 189)
        self.centralwidget = QtWidgets.QWidget(AddNodePage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.nodeheurestic = QtWidgets.QSpinBox(self.centralwidget)
        self.nodeheurestic.setGeometry(QtCore.QRect(130, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nodeheurestic.setFont(font)
        self.nodeheurestic.setObjectName("nodeheurestic")
        self.nodename = QtWidgets.QLineEdit(self.centralwidget)
        self.nodename.setGeometry(QtCore.QRect(130, 20, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nodename.setFont(font)
        self.nodename.setObjectName("nodename")
        self.confirmaddnode = QtWidgets.QPushButton(self.centralwidget)
        self.confirmaddnode.setGeometry(QtCore.QRect(130, 100, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.confirmaddnode.setFont(font)
        self.confirmaddnode.setObjectName("confirmaddnode")
        AddNodePage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddNodePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 252, 21))
        self.menubar.setObjectName("menubar")
        AddNodePage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddNodePage)
        self.statusbar.setObjectName("statusbar")
        AddNodePage.setStatusBar(self.statusbar)

        self.retranslateUi(AddNodePage)
        QtCore.QMetaObject.connectSlotsByName(AddNodePage)

    def retranslateUi(self, AddNodePage):
        _translate = QtCore.QCoreApplication.translate
        AddNodePage.setWindowTitle(_translate("AddNodePage", "Add Node"))
        self.label.setText(_translate("AddNodePage", "Name:"))
        self.label_2.setText(_translate("AddNodePage", "Heurestic:"))
        self.confirmaddnode.setText(_translate("AddNodePage", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddNodePage = QtWidgets.QMainWindow()
    ui = Ui_AddNodePage()
    ui.setupUi(AddNodePage)
    AddNodePage.show()
    sys.exit(app.exec_())
