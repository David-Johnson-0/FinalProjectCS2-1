from gui import *
import csv
import re
from PyQt6.QtWidgets import *
class Logic():
"""
Initializes the UI and ensures none of the buttons are checked by default while setting focus to the input space for candidates, num_votes are universal variables for counting votes
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
            if self.cand1.isChecked():
                writer.writerow(f'{self.candinput.text()}, str({self.candvote1.text()}))
            elif self.cand2.isChecked():
                writer.writerow(f'{self.candinput.text()}, str({self.candvote2.text()}))
            elif self.cand3.isChecked():
                writer.writerow(f'{self.candinput.text()}, str({self.candvote3.text()}))
            elif self.cand4.isChecked():
                writer.writerow(f'{self.candinput.text()}, str({self.candvote4.text()}))
            elif self.cand5.isChecked():
                writer.writerow(f'{self.candinput.text()}, str({self.candvote5.text()}))
"""
Closes the window and showcases final totals for the votes
"""
    def exit(self):
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if (self.cand1.text() != ''):
                writer.writerow(f'{self.cand1.text()}, str({self.candvote1.text()}))
            if (self.cand2.text() != ''):
                writer.writerow(f'{self.cand2.text()}, str({self.candvote2.text()}))
            if (self.cand3.text() != ''):
                writer.writerow(f'{self.cand3.text()}, str({self.candvote3.text()}))
            if (self.cand4.text() != ''):
                writer.writerow(f'{self.cand4.text()}, str({self.candvote4.text()}))
            if (self.cand5.text() != ''):
                writer.writerow(f'{self.cand5.text()}, str({self.candvote5.text()}))
        self.threadData()
"""
Submits the name of the candiate and puts it next to a vote button
"""
    def submit_candidate(self):
        if (self.cand1.text() == ''):
            cand1.setText(f'{candinput}')
        elif (self.cand2.text() == ''):
            cand2.setText(f'{candinput}')        
        elif (self.cand3.text() == ''):
            cand3.setText(f'{candinput}')        
        elif (self.cand4.text() == ''):
            cand4.setText(f'{candinput}')
        elif (self.cand5.text() == ''):
            cand5.setText(f'{candinput}')            
"""
Actively gets the number of votes for each candiate
"""
    def get_tally(self):
        with open('data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if self.cand1.isChecked():
                num_votes1 += 1
                self.candvote1.setText(str(num_votes1))
                for line in file:
                    line = line.split()
                    if re.search(f'^{cand1.text()}):
                        del line
                        writer.writerow(f'{self.candinput.text()}, str({self.candvote1.text()}))
            elif self.cand2.isChecked():
                num_votes2 += 1
                self.candvote2.setText(str(num_votes2))
                for line in file:
                    line = line.split()
                    if re.search(f'^{cand2.text()}):
                        del line
                        writer.writerow(f'{self.candinput.text()}, str({self.candvote2.text()}))
            elif self.cand3.isChecked():
                num_votes3 += 1
                self.candvote3.setText(str(num_votes3))
                for line in file:
                    line = line.split()
                    if re.search(f'^{cand3.text()}):
                        del line
                        writer.writerow(f'{self.candinput.text()}, str({self.candvote3.text()}))            
            elif self.cand4.isChecked():
                num_votes4 += 1
                self.candvote1.setText(str(num_votes4))
                for line in file:
                    line = line.split()
                    if re.search(f'^{cand4.text()}):
                        del line
                        writer.writerow(f'{self.candinput.text()}, str({self.candvote4.text()}))
            elif self.cand5.isChecked():
                num_votes5 += 1
                self.candvote5.setText(str(num_votes5))
                for line in file:
                    line = line.split()
                    if re.search(f'^{cand5.text()}):
                        del line
                        writer.writerow(f'{self.candinput.text()}, str({self.candvote5.text()}))
"""
Clears all inputs
"""
    def clear(self):
        self.candinput.clear()
        self.cand1.clear()
        self.cand2.clear()
        self.cand3.clear()
        self.cand4.clear()
        self.cand5.clear()
        self.candinput.setFocus()
