# imports the contents of the gui file, the csv methods, and the various methods of PyQt6
from gui import *
import csv
from PyQt6.QtWidgets import *
# Initializes the main window, sets up the connections of each button to their functions, and sets all the buttons and input areas to blank by default
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
# Checks which candidate is selected for the vote, then sames their name into the variable "name".
# Then, it opens the data.csv file, creates the reader, and increases the second variable in the row (the vote count) by one if the name matches the first variable in the row.
# Lastly, it creates a csvwriter, and writes the now updated information to the data.csv file before calling the get_tally and clear functions (to deselect the candidate).
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
    # First, it creates the list "rows" based on the data read by the csvreader while setting the default variables for total, winnerVal, and winnerName.
    # Then, the function enters a loop where it sets the variable current_text equal to whatever is in the infobox now, and the variable add_text to the string consisting of the name of the person in the row followed by the vote total.
    # When the rows conclude, the loop continues to the second part of the function.
    # The two strings are combined together in the variable new_text, which the text is then set to within infobox.
    # The total variable has the amount of the int version of row[1] added to it, while the variable winnerVal is compared to row[1].
    # If winnerVal is less than row[1], then both winnerVal and winnerName are set to the int(row[1]) and row[0] respectively.
    # It then creates the current_text variable and sets it to the current infobox text once more, and adds the winner's name, how many votes they have, and how many votes there were total.
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
# The variable name is set to whatever is in the candinput box, and focus is set to it if it is blank.
# The function then writes the candidate names to the csv file before clearing the candidates.
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
# First the function sets the text in the candidate names to none while opening the csvreader.
# It then sets the first not filled slot with the name input (ending if all are filled), then calls the get_tally function.
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
# Puts the total votes per candidate in the counting box.
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
    # Clears all selections and the input box while refocusing to it.
    def clear(self):
        self.cand1.setChecked(False)
        self.cand2.setChecked(False)
        self.cand3.setChecked(False)
        self.cand4.setChecked(False)
        self.cand5.setChecked(False)
        self.candinput.setText("")
        self.candinput.setFocus()
