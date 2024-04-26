from gui import *
import csv
from PyQt6.QtWidgets import *
class Logic():
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ExitButton.clicked.connect(lambda: self.exit())
        self.SubmitButton.clicked.connect(lambda: self.submit_candidate(), self.clear())
        self.VoteButton.clicked.connect(lambda: self.vote(), self.clear())
        self.cand1.setChecked(False)
        self.cand2.setChecked(False)
        self.cand3.setChecked(False)
        self.cand4.setChecked(False)
        self.cand5.setChecked(False)
        self.candinput.setFocus()

    def vote(self):
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
        pass
    def exit(self):
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
        pass
    def submit_candidate(self):
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
        pass
    def get_tally(self):
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
        pass
    def clear(self):
        pass