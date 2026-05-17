from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from .games import GamesUi

class LobbyUi(QWidget):
    def __init__(self):
        super().__init__()
        self.lobby_title = QLabel("Lobby")
        self.user_credits = QLabel("Credits: 0")
        self.home_button = QPushButton("Games")
        self.profile_button = QPushButton("Profile")
        self.settings_button = QPushButton("Settings")
        menu_layout = QHBoxLayout()
        menu_layout.addWidget(self.lobby_title)
        menu_layout.addStretch()
        menu_layout.addWidget(self.user_credits)
        menu_layout.addWidget(self.home_button)
        menu_layout.addWidget(self.profile_button)
        menu_layout.addWidget(self.settings_button)

        self.stack = QStackedWidget()
    
        self.games_page = GamesUi()
        self.stack.addWidget(self.games_page)

        layout = QVBoxLayout()
        layout.addLayout(menu_layout)
        layout.addStretch()
        layout.addWidget(self.stack)
        layout.addStretch()

        self.setLayout(layout)