#       Author- Jacob Stringer
#       Date started - January 22nd 2021

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QButtonGroup,
    QCheckBox,
)

from Randomized_Recursive_Backtracker import RRBMaze, Module
from Recursive_Division import RdMaze, Modules


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Maze Programs - Milamber")

        # variable to hold what algorithm to use when calculating the maze
        self.algorthm = RRBMaze.main()

        self.layout = QHBoxLayout(self)
        self.algorithmLayout = QVBoxLayout()

        self.alorithmSelector = QButtonGroup()
        self.alorithmSelector.setExclusive(True)
        self.alorithmSelector.buttonToggled.connect

        self.rRbSelector = QCheckBox("Randomized Recursive Backtracker")
        self.rRbSelector.setChecked(True)

        self.rDSelector = QCheckBox("Recursive Division")

        self.algorthmDict = {
            self.rRbSelector: RRBMaze.main(),
            self.rDSelector: RdMaze.main(),
        }

    def Select_Algorithm(self, i):
        if i:
            if self.rRbSelector.isChecked():
                self.algorthm = self.algorthmDict[self.rRbSelector]
            elif self.rDSelector.isChecked():
                self.algorthm = self.algorthmDict[self.rDSelector]


app = QApplication(["none"])

window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default

# Start the event loop.
app.exec_()

# Your application won't reach here until you exit and the event
# loop has stopped
print("Program Closed")
