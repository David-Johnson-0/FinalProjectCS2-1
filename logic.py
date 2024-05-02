from gui import *
import csv
from PyQt6.QtWidgets import *
class Logic():
"""
Initializes the UI and ensures none of the buttons are checked by default while setting focus to the input space for candidates
"""
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
"""
Writes the name of the candidate in a csvfile the function creates
"""
    def vote(self):
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
        pass
"""
Closes the window and showcases final totals for the votes
"""
    def exit(self):
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
        pass
"""
Submits the name of the candiate and puts it next to a vote button
"""
    def submit_candidate(self):
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
        pass
"""
Actively gets the number of votes for each candiate
"""
    def get_tally(self):
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
        pass
"""
Clears all inputs
"""
    def clear(self):
        pass
