from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from .games import GamesUi
from .settings import SettingsUi
from .profile import ProfileUI

class LobbyUi(QWidget):
    def __init__(self):
        super().__init__()
        self.lobby_title = QLabel("Lobby")
        self.user_credits = QLabel("Credits: 0")
        self.games_button = QPushButton("Games")
        self.profile_button = QPushButton("Profile")
        self.settings_button = QPushButton("Settings")
        menu_layout = QHBoxLayout()
        menu_layout.addWidget(self.lobby_title)
        menu_layout.addStretch()
        menu_layout.addWidget(self.user_credits)
        menu_layout.addWidget(self.games_button)
        menu_layout.addWidget(self.profile_button)
        menu_layout.addWidget(self.settings_button)

        self.stack = QStackedWidget()
    
        self.games_page = GamesUi()
        self.stack.addWidget(self.games_page)

        self.settings_page = SettingsUi()
        self.stack.addWidget(self.settings_page)

        self.profile_page = ProfileUI()
        self.stack.addWidget(self.profile_page)

        self.games_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.games_page))
        self.profile_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.profile_page))
        self.settings_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.settings_page))

        layout = QVBoxLayout()
        layout.addLayout(menu_layout)
        layout.addStretch()
        layout.addWidget(self.stack)
        layout.addStretch()

        self.setLayout(layout)