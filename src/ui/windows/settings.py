from PyQt6.QtWidgets import *

class SettingsUi(QWidget):
    def __init__(self):
        super().__init__()

        self.settings_title = QLabel("Settings")
        self.logout_button = QPushButton("Logout")

        vLayout = QVBoxLayout()
        vLayout.addStretch()
        vLayout.addWidget(self.settings_title)
        vLayout.addWidget(self.logout_button)
        vLayout.addStretch()
        hLayout = QHBoxLayout()
        hLayout.addStretch()
        hLayout.addLayout(vLayout)
        hLayout.addStretch()
        

        self.setLayout(hLayout)