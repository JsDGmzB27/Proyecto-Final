from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

images = ["assets\\ruleta.jpg", "assets\\slots.jpg", "assets\\blackjack.jpg"]

class GamesUi(QWidget):
    def __init__(self):
        super().__init__()

        self.games = []
        grid = QGridLayout()
        for i in range(3):
            button = QPushButton()
            button.setIcon(QIcon(images[i]))
            button.setIconSize(QSize(320, 280))
            button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            button.setStyleSheet("border: none; background-color: transparent;")
            button.setFlat(True)
            self.games.append(button)
            grid.addWidget(button, i//3, i%3)
        
        self.setLayout(grid)