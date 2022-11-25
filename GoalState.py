from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetGoalPage(object):
    def setupUi(self, SetGoalPage):
        SetGoalPage.setObjectName("SetGoalPage")
        SetGoalPage.resize(243, 143)
        self.centralwidget = QtWidgets.QWidget(SetGoalPage)
        self.centralwidget.setObjectName("centralwidget")
        self.listofGoals = QtWidgets.QComboBox(self.centralwidget)
        self.listofGoals.setGeometry(QtCore.QRect(130, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listofGoals.setFont(font)
        self.listofGoals.setObjectName("listofGoals")
        self.GraphTypeLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.GraphTypeLabel_2.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GraphTypeLabel_2.setFont(font)
        self.GraphTypeLabel_2.setObjectName("GraphTypeLabel_2")
        self.confirmAddGoal = QtWidgets.QPushButton(self.centralwidget)
        self.confirmAddGoal.setGeometry(QtCore.QRect(20, 60, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.confirmAddGoal.setFont(font)
        self.confirmAddGoal.setObjectName("confirmAddGoal")
        SetGoalPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SetGoalPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 243, 21))
        self.menubar.setObjectName("menubar")
        SetGoalPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SetGoalPage)
        self.statusbar.setObjectName("statusbar")
        SetGoalPage.setStatusBar(self.statusbar)

        self.retranslateUi(SetGoalPage)
        QtCore.QMetaObject.connectSlotsByName(SetGoalPage)

    def retranslateUi(self, SetGoalPage):
        _translate = QtCore.QCoreApplication.translate
        SetGoalPage.setWindowTitle(_translate("SetGoalPage", "Goal State"))
        self.GraphTypeLabel_2.setText(_translate("SetGoalPage", "Goal State"))
        self.confirmAddGoal.setText(_translate("SetGoalPage", "Add to Goal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SetGoalPage = QtWidgets.QMainWindow()
    ui = Ui_SetGoalPage()
    ui.setupUi(SetGoalPage)
    SetGoalPage.show()
    sys.exit(app.exec_())
