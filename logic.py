from gui import *
import csv
from PyQt6.QtWidgets import *
class Logic(QMainWindow, Ui_VotingForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ExitButton.clicked.connect(lambda: self.exit())
        self.SubmitButton.clicked.connect(lambda: self.submit_candidate())
        self.SubmitButton.clicked.connect(lambda: self.clear())
        self.VoteButton.clicked.connect(lambda: self.vote())
        self.VoteButton.clicked.connect(lambda: self.clear())
        self.cand1.setChecked(False)
        self.cand2.setChecked(False)
        self.cand3.setChecked(False)
        self.cand4.setChecked(False)
        self.cand5.setChecked(False)
        self.candinput.setFocus()
        self.candidates()
        self.infobox.setText(None)

    def vote(self):
        if self.cand1.isChecked():
            name = self.cand1.text()
        elif self.cand2.isChecked():
            name = self.cand2.text()
        elif self.cand3.isChecked():
            name = self.cand3.text()
        elif self.cand4.isChecked():
            name = self.cand4.text()
        elif self.cand5.isChecked():
            name = self.cand5.text()
        else:
            return None
        with open('data.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for row in rows:
                if row[0] == name:
                    row[1] = str(int(row[1]) + 1)

        with open('data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        self.get_tally()
        self.clear()
        pass
    def exit(self):
        with open('data.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            total = 0
            winnerVal = 0
            winnerName = None
            for row in rows:
                if row:
                    current_text = self.infobox.text()
                    add_text = f'{row[0]}...................................votes:{row[1]}'
                    new_text = current_text + '\n' + add_text
                    self.infobox.setText(new_text)
                    total += int(row[1])
                    if int(row[1]) > winnerVal:
                        winnerVal, winnerName = int(row[1]),row[0]
                else:
                    continue
            current_text = self.infobox.text()
            self.infobox.setText(f"{current_text}\n{winnerName} wins this vote with {winnerVal} votes\n"
                                 f" out of {total} total votes!")

    def submit_candidate(self):
        name = self.candinput.text()
        if not name:
            self.candinput.setFocus()
        if self.cand1.text() and self.cand2.text() and self.cand3.text() and self.cand4.text() and self.cand5.text():
            pass
        else:
            with open('data.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, 0])
            self.candidates()
            self.clear()
        pass

    def candidates(self):
        with open('data.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.cand1.setText(None)
            self.cand2.setText(None)
            self.cand3.setText(None)
            self.cand4.setText(None)
            self.cand5.setText(None)
            for row in rows:
                if not self.cand1.text():
                    self.cand1.setText(row[0])
                    pass
                elif not self.cand2.text():
                    self.cand2.setText(row[0])
                    pass
                elif not self.cand3.text():
                    self.cand3.setText(row[0])
                    pass
                elif not self.cand4.text():
                    self.cand4.setText(row[0])
                    pass
                elif not self.cand5.text():
                    self.cand5.setText(row[0])
                    pass
                else:
                    pass
        self.get_tally()
    def get_tally(self):
        with open('data.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for row in rows:
                if row[0] == self.cand1.text():
                    self.candvote1.setText(row[1])
                elif row[0] == self.cand2.text():
                    self.candvote2.setText(row[1])
                elif row[0] == self.cand3.text():
                    self.candvote3.setText(row[1])
                elif row[0] == self.cand4.text():
                    self.candvote4.setText(row[1])
                elif row[0] == self.cand5.text():
                    self.candvote5.setText(row[1])
        pass
    def clear(self):
        self.cand1.setChecked(False)
        self.cand2.setChecked(False)
        self.cand3.setChecked(False)
        self.cand4.setChecked(False)
        self.cand5.setChecked(False)
        self.candinput.setText("")
        self.candinput.setFocus()
