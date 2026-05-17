from PyQt6.QtWidgets import *

class LobbyUi(QWidget):
    def __init__(self):
        super().__init__()
        self.lobbyTitle = QLabel("Lobby")

        layout = QVBoxLayout()
        layout.addWidget(self.lobbyTitle)

        self.setLayout(layout)