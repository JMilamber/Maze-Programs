#       Author- Jacob Stringer
#       Date started - January 22nd 2021

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QButtonGroup,
    QCheckBox,
    QWidget,
    QPushButton,
    QLabel,
)

from Algorithms import RRBMaze
from Algorithms import RdMaze


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Maze Programs - Milamber")
        self.app = QWidget()

        # variable to hold what algorithm to use when calculating the maze
        self.algorithm = 0
        self.algorithmWait = 1

        self.Layout = QHBoxLayout(self.app)
        self.algorithmLayout = QVBoxLayout()
        self.detailslayout = QVBoxLayout()

        # Algorithm Layout Setup
        self.algorithmSelector = QButtonGroup()
        self.algorithmSelector.setExclusive(True)
        self.algorithmSelector.buttonToggled.connect(self.Select_Algorithm)

        self.rRbSelector = QCheckBox("Randomized Recursive Backtracker")
        self.rRbSelector.setChecked(True)

        self.rDSelector = QCheckBox("Recursive Division")

        self.eSelector = QCheckBox("Eller's")

        self.algorithmSelector.addButton(self.rRbSelector)
        self.algorithmSelector.addButton(self.rDSelector)
        self.algorithmSelector.addButton(self.eSelector)

        self.algorithmLayout.addWidget(self.rRbSelector)
        self.algorithmLayout.addWidget(self.rDSelector)
        self.algorithmLayout.addWidget(self.eSelector)

        self.Layout.addLayout(self.algorithmLayout)

        # Details Layout Setup

        self.size = QLabel("Size")
        self.hallSize = QLabel("HallSize")
        self.start = QPushButton("Start")
        self.start.clicked.connect(self.Start_Algorithm)

        self.detailslayout.addWidget(self.size)
        self.detailslayout.addWidget(self.hallSize)
        self.detailslayout.addWidget(self.start)

        self.Layout.addLayout(self.detailslayout)

        self.setCentralWidget(self.app)

    def Select_Algorithm(self):
        if self.algorithmWait:
            self.algorithmWait = 0
            if self.rRbSelector.isChecked():
                self.algorithm = 0
                print("RRB")
            elif self.rDSelector.isChecked():
                self.algorithm = 1
                print("Rd")
            elif self.eSelector.isChecked():
                self.algorithm = 2
                print("Eller")
        else:
            self.algorithmWait = 1

    def Start_Algorithm(self):
        i = self.algorithm
        if i == 0:
            RRBMaze.main()
        elif i == 1:
            RdMaze.draw(400, 10, "no")
        elif i == 2:
            print("Eller start")


app = QApplication(["none"])

window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default

# Start the event loop.
app.exec_()

# Your application won't reach here until you exit and the event
# loop has stopped
print("Program Closed")
