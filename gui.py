# Form implementation generated from reading ui file 'vote_gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VotingForm(object):
    def setupUi(self, VotingForm):
        VotingForm.setObjectName("VotingForm")
        VotingForm.resize(400, 800)
        VotingForm.setMinimumSize(QtCore.QSize(400, 800))
        VotingForm.setMaximumSize(QtCore.QSize(400, 800))
        self.centralwidget = QtWidgets.QWidget(parent=VotingForm)
        self.centralwidget.setObjectName("centralwidget")
        self.SubmitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(100, 130, 200, 50))
        self.SubmitButton.setMinimumSize(QtCore.QSize(200, 50))
        self.SubmitButton.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.SubmitButton.setCheckable(False)
        self.SubmitButton.setObjectName("SubmitButton")
        self.ExitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(240, 500, 100, 50))
        self.ExitButton.setMinimumSize(QtCore.QSize(100, 50))
        self.ExitButton.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.ExitButton.setFont(font)
        self.ExitButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ExitButton.setCheckable(False)
        self.ExitButton.setObjectName("ExitButton")
        self.cand1 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.cand1.setGeometry(QtCore.QRect(50, 190, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cand1.setFont(font)
        self.cand1.setText("")
        self.cand1.setObjectName("cand1")
        self.cand2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.cand2.setGeometry(QtCore.QRect(50, 240, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cand2.setFont(font)
        self.cand2.setText("")
        self.cand2.setObjectName("cand2")
        self.cand3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.cand3.setGeometry(QtCore.QRect(50, 290, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cand3.setFont(font)
        self.cand3.setText("")
        self.cand3.setObjectName("cand3")
        self.cand4 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.cand4.setGeometry(QtCore.QRect(50, 360, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cand4.setFont(font)
        self.cand4.setText("")
        self.cand4.setObjectName("cand4")
        self.cand5 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.cand5.setGeometry(QtCore.QRect(50, 410, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cand5.setFont(font)
        self.cand5.setText("")
        self.cand5.setObjectName("cand5")
        self.candinput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.candinput.setGeometry(QtCore.QRect(200, 40, 200, 50))
        self.candinput.setMinimumSize(QtCore.QSize(200, 50))
        self.candinput.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.candinput.setFont(font)
        self.candinput.setText("")
        self.candinput.setObjectName("candinput")
        self.VoteButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.VoteButton.setGeometry(QtCore.QRect(60, 500, 100, 50))
        self.VoteButton.setMinimumSize(QtCore.QSize(100, 50))
        self.VoteButton.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.VoteButton.setFont(font)
        self.VoteButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.VoteButton.setCheckable(False)
        self.VoteButton.setObjectName("VoteButton")
        self.candinputlabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.candinputlabel.setGeometry(QtCore.QRect(0, 50, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.candinputlabel.setFont(font)
        self.candinputlabel.setObjectName("candinputlabel")
        self.infobox = QtWidgets.QLabel(parent=self.centralwidget)
        self.infobox.setGeometry(QtCore.QRect(60, 580, 300, 150))
        self.infobox.setMinimumSize(QtCore.QSize(300, 150))
        self.infobox.setMaximumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.infobox.setFont(font)
        self.infobox.setText("")
        self.infobox.setObjectName("infobox")
        self.candvote1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.candvote1.setGeometry(QtCore.QRect(270, 180, 50, 50))
        self.candvote1.setMinimumSize(QtCore.QSize(50, 50))
        self.candvote1.setMaximumSize(QtCore.QSize(50, 50))
        self.candvote1.setText("")
        self.candvote1.setObjectName("candvote1")
        self.candvote2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.candvote2.setGeometry(QtCore.QRect(270, 230, 50, 50))
        self.candvote2.setMinimumSize(QtCore.QSize(50, 50))
        self.candvote2.setMaximumSize(QtCore.QSize(50, 50))
        self.candvote2.setText("")
        self.candvote2.setObjectName("candvote2")
        self.candvote3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.candvote3.setGeometry(QtCore.QRect(270, 290, 50, 50))
        self.candvote3.setMinimumSize(QtCore.QSize(50, 50))
        self.candvote3.setMaximumSize(QtCore.QSize(50, 50))
        self.candvote3.setText("")
        self.candvote3.setObjectName("candvote3")
        self.candvote4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.candvote4.setGeometry(QtCore.QRect(270, 340, 50, 50))
        self.candvote4.setMinimumSize(QtCore.QSize(50, 50))
        self.candvote4.setMaximumSize(QtCore.QSize(50, 50))
        self.candvote4.setText("")
        self.candvote4.setObjectName("candvote4")
        self.candvote5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.candvote5.setGeometry(QtCore.QRect(270, 400, 50, 50))
        self.candvote5.setMinimumSize(QtCore.QSize(50, 50))
        self.candvote5.setMaximumSize(QtCore.QSize(50, 50))
        self.candvote5.setText("")
        self.candvote5.setObjectName("candvote5")
        VotingForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=VotingForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        VotingForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=VotingForm)
        self.statusbar.setObjectName("statusbar")
        VotingForm.setStatusBar(self.statusbar)

        self.retranslateUi(VotingForm)
        QtCore.QMetaObject.connectSlotsByName(VotingForm)

    def retranslateUi(self, VotingForm):
        _translate = QtCore.QCoreApplication.translate
        VotingForm.setWindowTitle(_translate("VotingForm", "Voting Form"))
        self.SubmitButton.setText(_translate("VotingForm", "Submit"))
        self.ExitButton.setText(_translate("VotingForm", "Exit"))
        self.VoteButton.setText(_translate("VotingForm", "Vote"))
        self.candinputlabel.setText(_translate("VotingForm", "Enter candidate name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VotingForm = QtWidgets.QMainWindow()
    ui = Ui_VotingForm()
    ui.setupUi(VotingForm)
    VotingForm.show()
    sys.exit(app.exec())